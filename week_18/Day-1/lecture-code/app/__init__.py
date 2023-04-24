from flask import Flask, render_template  
from .config import Config
from .posts import posts



app = Flask(__name__)
print(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    """renders the site home page"""
    # Queries would go here
    # and data manipulation you want to do to that query
    return render_template("index.html")


@app.route("/all")
def get_all_posts():
    """route to fetch and display all posts"""
    # Query our DB to get all posts
    # posts = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given route param id"""
    # post = Post.query.get(id)
    one_post = [post for post in posts if post["id"] == id ]
    return render_template("feed.html", posts=one_post)


