import json

"""Helper to save video data to json"""
def save_data(data):
    json_str = json.dumps(data, indent=4)
    with open("./videos.json", "w") as f:
        f.write(json_str)

"""Helper to load video data from json"""
def load_data():
    with open("./videos.json", "r") as f:
        return json.load(f)
