from flask import Flask, render_template  
from .config import Config
from .posts import posts


app = Flask(__name__)

app.config.from_object(Config)

print(__name__)


@app.route("/")
def index():
    """renders the home page"""
    return render_template("index.html")



@app.route("/all")
def get_all_posts():
    """get all posts and display them"""
    # posts = Post.query.all()
    return render_template("feed.html", posts=posts)



@app.route("/post/<int:id>")
def get_post_by_id(id): 
    """return a single post by its ID"""
    print(id)
    one_post = [post for post in posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post)
       



