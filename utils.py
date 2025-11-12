import json

# Helper to save video data to json
def save_data(data):
    json_str = json.dumps(data, indent=4)
    with open("./videos.json", "w") as f:
        f.write(json_str)
