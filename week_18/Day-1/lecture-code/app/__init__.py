from flask import Flask, render_template
from .config import Config
from .posts import posts

app = Flask(__name__)
print(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    """home route will return the landing page"""
    # Query
    return render_template("index.html")


@app.route("/all")
def get_all_posts():
    """get all the posts and return them """
    # all_post = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    """return a single post by the id passed to the route"""
    # one_post = Post.query.get(id)
    one_post = [post for post in posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post )

