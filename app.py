import os
import json
from flask import Flask
from flask import render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv('SECRET_KEY') 

# Load videos data from json
with open("./videos.json", "r") as f:
    videos_data = json.load(f)

@app.route('/')
def home():
    return render_template('home.html')
