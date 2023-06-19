from flask import Flask, render_template 
from .config import Config
from .posts import posts


app = Flask(__name__)
print(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    """Landing page for our Patchstagram app"""
    # query for data
    # any other python logic we want
    # return render_template("index.html")
    return {"key": "some values"}


@app.route("/all")
def get_all_posts():
    """Query for all posts and render a template displaying them"""
    # posts = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    # one_posr = Post.query.get(id)
    one_post = [post for post in posts if post["id"] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)