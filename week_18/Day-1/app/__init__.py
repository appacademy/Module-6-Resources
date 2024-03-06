from flask import Flask, render_template, redirect
from app.config import Config
from .posts import users, posts
from app.routes.posts import post_routes
from app.routes.users import user_routes

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(post_routes, url_prefix="/posts")
app.register_blueprint(user_routes, url_prefix="/users")

# print(__name__)

@app.route("/")
def index():
    # print("I'm getting dizzy from all these redirects")
    return render_template("index.html")
    # return "<h1>Welcome to Pipstagram</h1>"

@app.route("/home")
def home():
    print("You are being redirected!!!!!")
    return redirect("/")


