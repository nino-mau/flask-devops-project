import os
import json
import uuid
from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
from dotenv import load_dotenv

from service.video import Video
from utils import load_data, save_data

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
    return render_template("video.html", video=video)


@app.route("/videos/add", methods=["POST", "GET"])
def add_video():
    if request.method == "POST":
        title = request.form["title"]
        url = request.form["url"]

        app.logger.info("%s title: ", title)
        app.logger.info("%s url: ", url)

        if not title:
            flash("Title is required!")
        elif not url:
            flash("Content is required!")
        else:
            videos_data.append({"id": str(uuid.uuid4()), "title": title, "url": url})
            save_data(videos_data)
            return redirect(url_for("home"))
    return render_template("videos-add.html")


@app.route("/videos/delete/<string:id>", methods=["POST"])
def delete_video(id):
    Video.delete(id)
    return redirect(url_for("home"))
