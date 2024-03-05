from flask import Flask, render_template
from app.config import Config
from .posts import users, posts

app = Flask(__name__)

app.config.from_object(Config)

# print(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    # return "<h1>Welcome to Pipstagram</h1>"

@app.route("/posts")
def all_posts():

    return render_template("all_posts.html", posts=posts)
    # return "posts coming soon"
    # return { post["id"]: post for post in posts }

@app.route("/posts/<int:id>")
def single_post(id):
    single_post = [posts[id]]
    print(single_post)
    # return "single_post"
    return render_template("all_posts.html", posts=single_post)
