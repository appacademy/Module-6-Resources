from flask import Flask, render_template, redirect 
from .config import Config
from .posts import posts 


app = Flask(__name__)
print(__name__)
app.config.from_object(Config)



@app.route('/')
def index():
    """render the home page"""
    return render_template("index.html")
    # return redirect("/another")
    # return {"important vals": ["one", "two", "three"]}


@app.route("/all")
def get_all_posts():
    """get all posts and return a feed of those posts"""
    # query posts = Post.query.all()
    # print(posts)
    sorted_posts = sorted(posts, key=lambda post: post["date"], reverse=True)
    return render_template("feed.html", posts=sorted_posts)



@app.route("/<int:id>")
def get_post_by_id(id):
    # post = Post.query.get(id)
    one_post = [post for post in posts if post['id'] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)


@app.route("/another")
def another_route():
    return "<h1>Another route</h1>"