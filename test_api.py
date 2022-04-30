import unittest
from urllib import response

import requests


TARGET_API = 'https://www.breakingbadapi.com/api/'
HTTP_OK = 200
TOTAL_CHARACTERS = 62

class TestMyAPI(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_fetch_all_characters(self):
        response = requests.get(f'{TARGET_API}characters')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(
            len(response.json()),\
            TOTAL_CHARACTERS,\
            f"Failed: expecting fetch data about {TOTAL_CHARACTERS} characters"
        )

    def test_fetch_first_character(self):
        response = requests.get(f'{TARGET_API}characters/1')
        self.assertEqual(response.status_code, HTTP_OK)
        data = (response.json())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['char_id'], 1)
        self.assertEqual(data[0]['name'], 'Walter White')

    def test_fetch_all_quotes_from_a_series(self):
        response = requests.get(f'{TARGET_API}quotes?series=Better+Call+Saul')
        self.assertEqual(response.status_code, HTTP_OK)
        print(response.json())



    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()