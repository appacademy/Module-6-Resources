from flask import Flask, render_template
from .posts import posts, users

from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/all")
def all_posts():
    return render_template("all-posts.html", posts=posts, id=None)

# @app.route("/<int:id>")
# def single_post(id):
#     return render_template("all-posts.html", posts=posts, id=id)

@app.route("/users/<int:id>")
def user_posts(id):
    user = list(filter(lambda x: x["id"] == id, users))[0]
    return render_template("all-posts.html", posts=posts, user=user)




    
