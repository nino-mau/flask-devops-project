import pytest
from unittest.mock import patch, MagicMock
from service.video import Video


@pytest.fixture
def sample_videos():
    """Fixture providing sample video data"""
    return [
        {
            "id": "123",
            "title": "Test Video 1",
            "url": "https://youtube.com/watch?v=test1",
        },
        {
            "id": "456",
            "title": "Test Video 2",
            "url": "https://youtube.com/watch?v=test2",
        },
        {
            "id": "789",
            "title": "Test Video 3",
            "url": "https://youtube.com/watch?v=test3",
        },
    ]


class TestVideoGet:
    """Test suite for Video.get() method"""

    @patch("service.video.load_data")
    def test_get_existing_video(self, mock_load_data, sample_videos):
        """Test getting a video that exists"""
        mock_load_data.return_value = sample_videos

        result = Video.get("456")

        assert result is not None
        assert result["id"] == "456"
        assert result["title"] == "Test Video 2"
        assert result["url"] == "https://youtube.com/watch?v=test2"

    @patch("service.video.load_data")
    def test_get_non_existing_video(self, mock_load_data, sample_videos):
        """Test getting a video that doesn't exist"""
        mock_load_data.return_value = sample_videos

        result = Video.get("999")

        assert result is None

    @patch("service.video.load_data")
    def test_get_from_empty_list(self, mock_load_data):
        """Test getting a video from empty list"""
        mock_load_data.return_value = []

        result = Video.get("123")

        assert result is None

    @patch("service.video.load_data")
    def test_get_first_video(self, mock_load_data, sample_videos):
        """Test getting the first video in the list"""
        mock_load_data.return_value = sample_videos

        result = Video.get("123")

        assert result is not None
        assert result["id"] == "123"

    @patch("service.video.load_data")
    def test_get_last_video(self, mock_load_data, sample_videos):
        """Test getting the last video in the list"""
        mock_load_data.return_value = sample_videos

        result = Video.get("789")

        assert result is not None
        assert result["id"] == "789"


class TestVideoAdd:
    """Test suite for Video.add() method"""

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_add_video(self, mock_load_data, mock_save_data, sample_videos):
        """Test adding a new video"""
        mock_load_data.return_value = sample_videos.copy()

        Video.add("New Video", "https://youtube.com/watch?v=new")

        # Verify load_data was called
        mock_load_data.assert_called_once()

        # Verify save_data was called
        mock_save_data.assert_called_once()

        # Check that the saved data includes the new video
        saved_data = mock_save_data.call_args[0][0]
        assert len(saved_data) == 4
        assert saved_data[-1]["title"] == "New Video"
        assert saved_data[-1]["url"] == "https://youtube.com/watch?v=new"
        assert "id" in saved_data[-1]

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_add_video_to_empty_list(self, mock_load_data, mock_save_data):
        """Test adding a video to an empty list"""
        mock_load_data.return_value = []

        Video.add("First Video", "https://youtube.com/watch?v=first")

        saved_data = mock_save_data.call_args[0][0]
        assert len(saved_data) == 1
        assert saved_data[0]["title"] == "First Video"

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_add_video_generates_unique_id(
        self, mock_load_data, mock_save_data, sample_videos
    ):
        """Test that adding a video generates a unique ID"""
        mock_load_data.return_value = sample_videos.copy()

        Video.add("Unique Video", "https://youtube.com/watch?v=unique")

        saved_data = mock_save_data.call_args[0][0]
        new_video = saved_data[-1]

        # Check that ID is generated and is unique
        assert "id" in new_video
        assert new_video["id"] not in ["123", "456", "789"]


class TestVideoDelete:
    """Test suite for Video.delete() method"""

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_delete_existing_video(self, mock_load_data, mock_save_data, sample_videos):
        """Test deleting a video that exists"""
        mock_load_data.return_value = sample_videos.copy()

        Video.delete("456")

        # Verify save_data was called
        mock_save_data.assert_called_once()

        # Check that the deleted video is not in saved data
        saved_data = mock_save_data.call_args[0][0]
        assert len(saved_data) == 2
        assert "456" not in [v["id"] for v in saved_data]

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_delete_non_existing_video(
        self, mock_load_data, mock_save_data, sample_videos
    ):
        """Test deleting a video that doesn't exist"""
        mock_load_data.return_value = sample_videos.copy()

        Video.delete("999")

        # Verify save_data was not called since video doesn't exist
        mock_save_data.assert_not_called()

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_delete_first_video(self, mock_load_data, mock_save_data, sample_videos):
        """Test deleting the first video in the list"""
        mock_load_data.return_value = sample_videos.copy()

        Video.delete("123")

        saved_data = mock_save_data.call_args[0][0]
        assert len(saved_data) == 2
        assert "123" not in [v["id"] for v in saved_data]

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_delete_last_video(self, mock_load_data, mock_save_data, sample_videos):
        """Test deleting the last video in the list"""
        mock_load_data.return_value = sample_videos.copy()

        Video.delete("789")

        saved_data = mock_save_data.call_args[0][0]
        assert len(saved_data) == 2
        assert "789" not in [v["id"] for v in saved_data]


class TestVideoUpdate:
    """Test suite for Video.update() method"""

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_update_existing_video(self, mock_load_data, mock_save_data, sample_videos):
        """Test updating a video that exists"""
        mock_load_data.return_value = sample_videos.copy()

        Video.update("456", "Updated Title", "https://youtube.com/watch?v=updated")

        # Verify save_data was called
        mock_save_data.assert_called_once()

        # Check that the video was updated
        saved_data = mock_save_data.call_args[0][0]
        updated_video = next(v for v in saved_data if v["id"] == "456")
        assert updated_video["title"] == "Updated Title"
        assert updated_video["url"] == "https://youtube.com/watch?v=updated"

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_update_non_existing_video(
        self, mock_load_data, mock_save_data, sample_videos
    ):
        """Test updating a video that doesn't exist"""
        mock_load_data.return_value = sample_videos.copy()

        Video.update("999", "Non-existent", "https://youtube.com/watch?v=none")

        # Verify save_data was not called since video doesn't exist
        mock_save_data.assert_not_called()

    @patch("service.video.save_data")
    @patch("service.video.load_data")
    def test_update_preserves_id(self, mock_load_data, mock_save_data, sample_videos):
        """Test that updating preserves the video ID"""
        mock_load_data.return_value = sample_videos.copy()

        Video.update("456", "New Title", "https://youtube.com/watch?v=new")

        saved_data = mock_save_data.call_args[0][0]
        updated_video = next(v for v in saved_data if v["id"] == "456")
        assert updated_video["id"] == "456"
