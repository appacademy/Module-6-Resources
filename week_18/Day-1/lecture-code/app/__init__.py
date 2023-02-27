from flask import Flask, render_template 
from .config import Config
from .posts import posts


app = Flask(__name__)
print(__name__)

app.config.from_object(Config)



@app.route("/")
def index():
    """renders the home page"""
    return render_template("index.html")


@app.route("/all")
def get_all_posts():
    # Query for all posts
    # posts = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    print(id)
    # Query
    # post=Post.query.get(id)
    one_post = [post for post in posts if post['id'] == id]
    return render_template("feed.html", posts=one_post)

