from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/videos', methods=['GET'])
def videos():
    ytb_prefix = 'https://www.youtube.com/embed/watch?v='
    urls = ['Rof660OEA3E', 'yakOBIoyoik']

    urls = [ytb_prefix + url for url in urls]
    print(urls)
    return render_template('videos.html', urls=urls)

#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"
#     return "<p>Videos Page</p>"

# Source - https://stackoverflow.com/a
# Posted by codegeek, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-12, License - CC BY-SA 4.0

app.run(debug=True)
if __name__ == "__main__":
    app.run