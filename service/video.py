import uuid
from utils import load_data, save_data


class Video:
    """
    Add a video
    """

    @staticmethod
    def add(title, url):
        videos = load_data()
        videos.append({"id": str(uuid.uuid4()), "title": title, "url": url})
        save_data(videos)

    """
    Return a video by it's id
    """

    @staticmethod
    def get(id):
        videos = load_data()
        for video in videos:
            if video["id"] == id:
                return video
        return None

    """
    Delete a video by it's id
    """

    @staticmethod
    def delete(id):
        videos = load_data()
        for i in range(len(videos)):
            video = videos[i]
            if video["id"] == id:
                videos.pop(i)
                save_data(videos)
                break
