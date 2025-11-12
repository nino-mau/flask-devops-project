import unittest
from unittest.mock import patch, MagicMock
from service.video import Video


class TestVideo(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.test_videos = [
            {"id": "123", "title": "Test Video 1", "url": "https://youtube.com/watch?v=test1"},
            {"id": "456", "title": "Test Video 2", "url": "https://youtube.com/watch?v=test2"},
            {"id": "789", "title": "Test Video 3", "url": "https://youtube.com/watch?v=test3"},
        ]

    @patch('service.video.load_data')
    def test_get_existing_video(self, mock_load_data):
        """Test getting a video that exists"""
        mock_load_data.return_value = self.test_videos
        
        result = Video.get("456")
        
        self.assertIsNotNone(result)
        if result:
            self.assertEqual(result["id"], "456")
            self.assertEqual(result["title"], "Test Video 2")
            self.assertEqual(result["url"], "https://youtube.com/watch?v=test2")

    @patch('service.video.load_data')
    def test_get_non_existing_video(self, mock_load_data):
        """Test getting a video that doesn't exist"""
        mock_load_data.return_value = self.test_videos
        
        result = Video.get("999")
        
        self.assertIsNone(result)

    @patch('service.video.load_data')
    def test_get_from_empty_list(self, mock_load_data):
        """Test getting a video from empty list"""
        mock_load_data.return_value = []
        
        result = Video.get("123")
        
        self.assertIsNone(result)

    @patch('service.video.save_data')
    @patch('service.video.load_data')
    def test_add_video(self, mock_load_data, mock_save_data):
        """Test adding a new video"""
        mock_load_data.return_value = self.test_videos.copy()
        
        Video.add("New Video", "https://youtube.com/watch?v=new")
        
        # Verify load_data was called
        mock_load_data.assert_called_once()
        
        # Verify save_data was called
        mock_save_data.assert_called_once()
        
        # Check that the saved data includes the new video
        saved_data = mock_save_data.call_args[0][0]
        self.assertEqual(len(saved_data), 4)
        self.assertEqual(saved_data[-1]["title"], "New Video")
        self.assertEqual(saved_data[-1]["url"], "https://youtube.com/watch?v=new")
        self.assertIn("id", saved_data[-1])

    @patch('service.video.save_data')
    @patch('service.video.load_data')
    def test_delete_existing_video(self, mock_load_data, mock_save_data):
        """Test deleting a video that exists"""
        mock_load_data.return_value = self.test_videos.copy()
        
        Video.delete("456")
        
        # Verify save_data was called
        mock_save_data.assert_called_once()
        
        # Check that the deleted video is not in saved data
        saved_data = mock_save_data.call_args[0][0]
        self.assertEqual(len(saved_data), 2)
        self.assertNotIn("456", [v["id"] for v in saved_data])

    @patch('service.video.save_data')
    @patch('service.video.load_data')
    def test_delete_non_existing_video(self, mock_load_data, mock_save_data):
        """Test deleting a video that doesn't exist"""
        mock_load_data.return_value = self.test_videos.copy()
        
        Video.delete("999")
        
        # Verify save_data was not called since video doesn't exist
        mock_save_data.assert_not_called()

    @patch('service.video.load_data')
    def test_get_first_video(self, mock_load_data):
        """Test getting the first video in the list"""
        mock_load_data.return_value = self.test_videos
        
        result = Video.get("123")
        
        self.assertIsNotNone(result)
        if result:
            self.assertEqual(result["id"], "123")

    @patch('service.video.load_data')
    def test_get_last_video(self, mock_load_data):
        """Test getting the last video in the list"""
        mock_load_data.return_value = self.test_videos
        
        result = Video.get("789")
        
        self.assertIsNotNone(result)
        if result:
            self.assertEqual(result["id"], "789")


if __name__ == "__main__":
    unittest.main()
