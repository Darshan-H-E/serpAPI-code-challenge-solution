import unittest
from parser import ArtworkParser

class TestFantasticParser(unittest.TestCase):
    def setUp(self):
        self.parser = ArtworkParser()

    def _assert_valid_artworks(self, artworks):
        self.assertIsInstance(artworks, list, "Artworks should be a list.")
        self.assertTrue(len(artworks) > 0, "Artworks list should not be empty.")

        for artwork in artworks:
            self.assertIsInstance(artwork, dict, "Each artwork should be a dictionary.")

            # Validate 'name' field
            self.assertIn('name', artwork, "'name' field is missing.")
            self.assertIsInstance(artwork['name'], str, "'name' should be a string.")
            self.assertTrue(len(artwork['name']) > 0, "'name' should not be empty.")

            # Validate 'link' field
            self.assertIn('link', artwork, "'link' field is missing.")
            self.assertIsInstance(artwork['link'], str, "'link' should be a string.")
            self.assertTrue(len(artwork['link']) > 0, "'link' should not be empty.")

            # Validate 'image' field
            self.assertIn('image', artwork, "'image' field is missing.")
            self.assertIsInstance(artwork['image'], str, "'image' should be a string.")
            self.assertTrue(len(artwork['image']) > 0, "'image' should not be empty.")

    def _test_parse_file(self, source):
        self.parser.parse_html_file(source)
        result = self.parser.get_data_as_dict()

        # Validate result structure
        self.assertIsInstance(result, dict, "Result should be a dictionary.")
        self.assertIn('artworks', result, "'artworks' field is missing in result.")

        # Validate artworks
        self._assert_valid_artworks(result['artworks'])

    def test_parse_files(self):
        sources = [
            "files/van-gogh-paintings.html",
            "files/d.html"
        ]
        for source in sources:
            with self.subTest(source=source):
                self._test_parse_file(source)

if __name__ == '__main__':
    unittest.main()
