from flask import Flask, render_template, url_for, redirect
from .config import Config
from .posts import posts
from .api.post_routes import post_routes

app = Flask(__name__)

print(__name__)

app.config.from_object(Config)

app.register_blueprint(post_routes)

@app.route("/")
def index():
  return render_template("index.html", title="Pipstagram")

  


@app.route("/redirect")
def route_redirect():
  return redirect(url_for("post_routes.feed"))