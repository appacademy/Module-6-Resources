from flask import Flask, render_template
from .config import Config
from .posts import posts

app = Flask(__name__)

print(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
  return render_template("index.html", title="Pipstagram")

  
@app.route("/feed")
def feed():
  return render_template("feed.html", posts=posts)