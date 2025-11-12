import os
import json
import uuid
from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
from dotenv import load_dotenv

from service.video import Video
from utils import get_video_metadata, load_data, save_data, url_to_embed

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Load videos data from json
videos_data = load_data()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/videos/<string:id>")
def video(id):
    video = Video.get(id)

    if video:
        metadata = get_video_metadata(video["url"])
        return render_template("video.html", video=video, metadata=metadata)

    return "bad request!", 400


@app.route("/videos/add", methods=["POST", "GET"])
def add_video():
    if request.method == "POST":
        title = request.form["title"]
        url = url_to_embed(request.form["url"])

        app.logger.info("%s title: ", title)
        app.logger.info("%s url: ", url)

        if not title:
            flash("Title is required!")
        elif not url:
            flash("Content is required!")
        else:
            Video.add(title, url)
            return redirect(url_for("home"))
    return render_template("videos-add.html")


@app.route("/videos", methods=["GET"])
def videos():
    ytb_prefix = "https://www.youtube.com/embed/"

    # Temp
    urls = ["Rof660OEA3E", "yakOBIoyoik", "56K5mhMf0ww", "nBHv7wYOi3I"]
    # Temp

    urls = [ytb_prefix + url for url in urls]
    print(urls)
    return render_template("videos.html", urls=urls)


@app.route("/videos/delete/<string:id>", methods=["POST"])
def delete_video(id):
    Video.delete(id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
