import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

from service.video import Video
from utils import get_video_metadata, load_data, url_to_embed

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

    return render_template("error.html", code="400", message="Bad Request")


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


@app.route("/videos/update/<string:id>", methods=["POST", "GET"])
def update_video(id):
    video = Video.get(id)

    if not video:
        return render_template("error.html", code="400", message="Bad Request")

    if request.method == "POST":
        title = request.form["title"]
        url = url_to_embed(request.form["url"])

        if not title:
            flash("Title is required!")
        elif not url:
            flash("Content is required!")
        else:
            Video.update(id, title, url)
            return redirect(url_for("video", id=id))

    return render_template("video-update.html", defaults=video)


if __name__ == "__main__":
    app.run(debug=True)
