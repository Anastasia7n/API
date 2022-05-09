import unittest
import requests

TARGET_API = "https://breakingbadapi.com/api/"
HTTP_OK = 200
TOTAL_CHARACTERS = 62

class TestMyAPI(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_fetch_all_characters(self):
        response = requests.get(f'{TARGET_API}characters')
        self.assertEqual( HTTP_OK, response.status_code)
        self.assertEqual(TOTAL_CHARACTERS, len(response.json()), f'Failed: expecting {TOTAL_CHARACTERS} characters!')

    def test_fetch_all_character_one(self):
        response = requests.get(f'{TARGET_API}characters/1')
        self.assertEqual(HTTP_OK, response.status_code)
        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual1, (data[0]['char_id'])
        self.assertEqual("Walter White", data[0]['name'] )
        print(response.json())

    def test_fetch_all_auotes_from_a_series(self):
        response = requests.get(f'{TARGET_API}quotes?series=Better+Call+Saul')
        self.assertEqual(HTTP_OK, response.status_code)
        # print(response.json())
        self.assertEqual(
			18,
            len(response.json()),
            'Failed: expecting 18 quotes from Better Call Saul series!'
        )

    def tearDown(self) -> None:
        pass


if __name__=='__main__':
    unittest.main()