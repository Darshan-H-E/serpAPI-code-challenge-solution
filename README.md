# Extract Van Gogh Paintings Code Challenge

Goal is to extract a list of Van Gogh paintings from the attached Google search results page.

![Van Gogh paintings](https://github.com/serpapi/code-challenge/blob/master/files/van-gogh-paintings.png?raw=true "Van Gogh paintings")

## Instructions

This is already fully supported on SerpApi. ([relevant test], [html file], [sample json], and [expected array].)
Try to come up with your own solution and your own test.
Extract the painting `name`, `extensions` array (date), and Google `link` in an array.

Fork this repository and make a PR when ready.

Programming language wise, Ruby (with RSpec tests) is strongly suggested but feel free to use whatever you feel like.

Parse directly the HTML result page ([html file]) in this repository. No extra HTTP requests should be needed for anything.

[relevant test]: https://github.com/serpapi/test-knowledge-graph-desktop/blob/master/spec/knowledge_graph_claude_monet_paintings_spec.rb
[sample json]: https://raw.githubusercontent.com/serpapi/code-challenge/master/files/van-gogh-paintings.json
[html file]: https://raw.githubusercontent.com/serpapi/code-challenge/master/files/van-gogh-paintings.html
[expected array]: https://raw.githubusercontent.com/serpapi/code-challenge/master/files/expected-array.json

Add also to your array the painting thumbnails present in the result page file (not the ones where extra requests are needed). 

Test against 2 other similar result pages to make sure it works against different layouts. (Pages that contain the same kind of carrousel. Don't necessarily have to be paintings.)

The suggested time for this challenge is 4 hours. But, you can take your time and work more on it if you want.

# Solution
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)

## Features

- **HTML Parsing:** Utilizes BeautifulSoup to navigate and extract relevant data from HTML files.
- **Data Extraction:** Extracts artwork names, links, images and extensions ensuring comprehensive data collection.
- **JSON Export:** Saves the extracted data into well-structured JSON files for easy integration and analysis.
- **Automated Testing:** Includes unit tests to ensure the reliability and accuracy of the parsing process.
- **Extensible Design:** Easily adaptable to parse different HTML structures or extract additional data fields.

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/Darshan-H-E/serpAPI-code-challenge-solution
cd serpAPI-code-challenge-solution/
```

### Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Prepare Your HTML Files

Ensure your HTML files are placed in the `files/` directory. For example:

```
files/
├── van-gogh-paintings.html
├── michelangelo-paintings.html
└── ...
```

### Run the Parser

Execute the `main.py` script to parse an HTML file and save the extracted data to JSON.

```bash
python main.py
```

*By default, `main.py` is set to parse `files/michelangelo-paintings.html`. To parse a different file, modify the `input_file_path` variable in `main.py`.*

### Output

The parsed data will be saved in the `output/` directory as a JSON file named after the source HTML file. For example:

```
output/
└── michelangelo-paintings.json
```

## Project Structure

```
serpAPI-code-challenge-solution/
├── files/
│   ├── van-gogh-paintings.html
│   ├── michelangelo-paintings.html
│   └── ...
├── output/
│   └── *.json
├── main.py
├── parser.py
├── test_parser.py
├── requirements.txt
├── README.md
└── LICENSE
```

- **main.py**: Entry point of the application. Initializes the parser and triggers the JSON export.
- **parser.py**: Contains the `ArtworkParser` class responsible for parsing HTML files and extracting data.
- **test_parser.py**: Includes unit tests to validate the functionality of `ArtworkParser`.
- **files/**: Directory containing the source HTML files to be parsed.
- **output/**: Directory where the resulting JSON files are saved.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **README.md**: Project documentation.
- **LICENSE**: License information.

## Running Tests

The project includes a suite of unit tests to ensure the parser works as expected.

### Execute Tests

```bash
python -m unittest test_parser.py
```

*Alternatively, you can run:*

```bash
python test_parser.py
```

### Test Coverage

The tests cover:

- Successful parsing of valid HTML files.
- Validation of extracted data fields (`name`, `link`, `image`).
- Handling of incomplete or malformed HTML elements.