from flask import Flask, render_template, redirect

from .posts import posts, users
from app.routes.post_routes import post_routes
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(post_routes, url_prefix="/posts")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect('/', 302)

