import unittest
import json
import os
import tempfile
from unittest.mock import patch, mock_open
from utils import load_data, save_data


class TestUtils(unittest.TestCase):
    def test_save_data(self):
        test_data = [
            {"id": "123", "title": "Test Video", "url": "https://example.com/video1"},
            {
                "id": "456",
                "title": "Another Video",
                "url": "https://example.com/video2",
            },
        ]
        expected_json = json.dumps(test_data, indent=4)

        with patch("builtins.open", mock_open()) as mock_file:
            save_data(test_data)

            # Verify open was called with correct parameters
            mock_file.assert_called_once_with("./videos.json", "w")

            # Verify write was called with correct JSON string
            handle = mock_file()
            handle.write.assert_called_once_with(expected_json)

    def test_load_data(self):
        test_data = [
            {"id": "123", "title": "Test Video", "url": "https://example.com/video1"},
            {
                "id": "456",
                "title": "Another Video",
                "url": "https://example.com/video2",
            },
        ]
        test_json = json.dumps(test_data, indent=4)

        with patch("builtins.open", mock_open(read_data=test_json)) as mock_file:
            videos_data = load_data()

            # Verify open was called with correct parameters
            mock_file.assert_called_once_with("./videos.json", "r")

            # Verify the loaded data matches expected data
            self.assertEqual(videos_data, test_data)


if __name__ == "__main__":
    unittest.main()
