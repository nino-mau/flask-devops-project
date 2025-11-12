import json
import yt_dlp

"""
Helper to save video data to json
"""


def save_data(data):
    json_str = json.dumps(data, indent=4)
    with open("./videos.json", "w") as f:
        f.write(json_str)


"""
Helper to load video data from json
"""


def load_data():
    with open("./videos.json", "r") as f:
        return json.load(f)


"""
Helper to get metadata of a video, return a dict
"""


def get_video_metadata(url):
    # url = embed_to_url(url)
    try:
        with yt_dlp.YoutubeDL(
            params={"quiet": True, "no_warnings": True, "extract_flat": False}
        ) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "views": info.get("view_count", 0),
                "author": info.get("uploader", "Unknown"),
            }
    except Exception as e:
        return {"views": 0, "author": "Unknown"}


"""
Helper to convert a youtube url to an embed youtube url
"""


def url_to_embed(url):
    return url.replace("watch?v=", "embed/")
