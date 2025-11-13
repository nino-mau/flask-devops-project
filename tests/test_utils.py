import json
import pytest
from unittest.mock import patch, mock_open
from utils import load_data, save_data


class TestUtils:
    """Test suite for utility functions"""

    def test_save_data(self):
        """Test saving data to JSON file"""
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
        """Test loading data from JSON file"""
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
            assert videos_data == test_data

    def test_save_data_empty_list(self):
        """Test saving empty list to JSON file"""
        test_data = []
        expected_json = json.dumps(test_data, indent=4)

        with patch("builtins.open", mock_open()) as mock_file:
            save_data(test_data)

            mock_file.assert_called_once_with("./videos.json", "w")
            handle = mock_file()
            handle.write.assert_called_once_with(expected_json)

    def test_load_data_empty_file(self):
        """Test loading data from empty JSON file"""
        test_json = json.dumps([])

        with patch("builtins.open", mock_open(read_data=test_json)) as mock_file:
            videos_data = load_data()

            assert videos_data == []

    def test_save_data_with_special_characters(self):
        """Test saving data with special characters"""
        test_data = [
            {
                "id": "123",
                "title": "Test & Special <Characters>",
                "url": "https://example.com/video?id=123&param=value",
            }
        ]
        expected_json = json.dumps(test_data, indent=4)

        with patch("builtins.open", mock_open()) as mock_file:
            save_data(test_data)

            handle = mock_file()
            handle.write.assert_called_once_with(expected_json)
