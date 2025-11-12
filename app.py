from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/videos', methods=['GET'])
def videos():
    urls = ['https://www.youtube.com/embed/watch?v=Rof660OEA3E', 
            'https://www.youtube.com/embed/watch?v=yakOBIoyoik']
    return render_template('videos.html', urls=urls)

#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"
#     return "<p>Videos Page</p>"