from utils import load_data, save_data


class Video:
    """
    Return a video by it's id
    """

    @staticmethod
    def get(id):
        videos = load_data()
        for video in videos:
            if video["id"] == id:
                return video

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
