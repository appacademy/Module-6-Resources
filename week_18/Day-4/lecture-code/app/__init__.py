from flask import Flask, render_template, url_for, redirect
from flask_migrate import Migrate
from .config import Config
from .posts import posts
from .api.post_routes import post_routes
from app.models import db


app = Flask(__name__)

# print(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(post_routes)

Migrate(app, db)

@app.route("/")
def index():
  return render_template("index.html", title="Pipstagram")

  


@app.route("/redirect")
def route_redirect():
  return redirect(url_for("post_routes.feed"))