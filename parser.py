import re
import json
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Optional, Dict, Any


class ArtworkParser:
    DATA_IMAGE_REGEX = re.compile(r"s='data:image[^']+'")
    SINGLE_QUOTE_STRING_REGEX = re.compile(r"'([^']+)'")

    def __init__(self, html_file_path: Optional[str] = None):
        self.soup: Optional[BeautifulSoup] = None
        self.parsed_data: Optional[Dict[str, Any]] = None
        self.file_path: Optional[Path] = None
        if html_file_path:
            self.file_path = Path(html_file_path)
            self.parse_html_file(html_file_path)

    def save_to_json(self) -> None:
        """Saves the parsed data to a JSON file in the 'output' directory."""
        output_directory = Path("output")
        output_directory.mkdir(exist_ok=True)
        
        json_file_path = output_directory / f"{self.file_path.stem}.json"
        try:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.parsed_data, json_file, indent=2, ensure_ascii=False)
            print(f"Successfully saved results to {json_file_path}")
        except IOError as error:
            print(f"Error writing to {json_file_path}: {error}")

    def get_data_as_dict(self) -> Dict[str, Any]:
        """Returns the parsed data as a dictionary."""
        return self.parsed_data or {}

    def parse_html_file(self, html_file_path: str) -> Dict[str, Any]:
        """Parses the HTML file to extract artwork information."""
        self._load_html_content(html_file_path)

        # Extract data images and create a mapping from ID to image data
        data_image_mapping = self._extract_data_images()

        # Extract and parse each artwork element
        artworks = [
            self._parse_single_artwork(element, data_image_mapping)
            for element in self.soup.select('div.iELo6')
        ]

        # Remove any None entries resulting from incomplete data
        artworks = [artwork for artwork in artworks if artwork]

        self.parsed_data = {'artworks': artworks}
        return self.parsed_data

    def _extract_data_images(self) -> Dict[str, str]:
        """Extracts data images from script tags and maps them by their IDs."""
        data_image_map: Dict[str, str] = {}
        script_tags = self.soup.find_all('script', string=self.DATA_IMAGE_REGEX)

        for script in script_tags:
            extracted_strings = self.SINGLE_QUOTE_STRING_REGEX.findall(script.string or "")
            if len(extracted_strings) >= 2:
                image_data, image_id = extracted_strings[:2]
                data_image_map[image_id] = image_data

        return data_image_map

    def _parse_single_artwork(self, artwork_element: BeautifulSoup, data_image_map: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Parses a single artwork HTML element to extract relevant information."""
        image_tag = artwork_element.find('img')
        if not image_tag:
            return None

        image_id = image_tag.get('id')
        image_source = image_tag.get('data-src') or image_tag.get('src')
        image_url = data_image_map.get(image_id, image_source)

        name_element = artwork_element.select_one('div.pgNMRc')
        link_element = artwork_element.find('a')
        extensions_element = artwork_element.select_one('div.cxzHyb')

        if not name_element or not link_element:
            return None

        artwork_data: Dict[str, Any] = {
            'name': name_element.get_text(strip=True),
            'link': f"https://google.com{link_element.get('href', '')}",
            'image': image_url,
        }

        extensions_text = extensions_element.get_text(strip=True) if extensions_element else ''
        if extensions_text:
            artwork_data['extensions'] = [extensions_text]

        return artwork_data

    def _load_html_content(self, html_file_path: str) -> None:
        """Loads and parses HTML content from a local file."""
        try:
            with open(html_file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()
            self.soup = BeautifulSoup(html_content, 'html.parser')
        except FileNotFoundError:
            raise ValueError(f"The file was not found: {html_file_path}")
