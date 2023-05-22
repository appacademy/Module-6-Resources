from flask import Flask, render_template  
from .config import Config
from .posts import posts



app = Flask(__name__)
print(__name__)

app.config.from_object(Config)



@app.route("/")
def index():
    """Landing page"""
    # Query the DB
    # return "<h1>Welcome to our flask server!</h1>"
    return render_template("index.html", title="Patchstagram")



@app.route("/all")
def feed():
    """Get all post and send to template for display"""
    # Query for all posts
    # all_posts = Post.query.all()
    return render_template("feed.html", posts = posts)



@app.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by its id"""
    # onme_post = Post.query.get(id)
    print(id)
    one_post = [post for post in posts if post['id'] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post)