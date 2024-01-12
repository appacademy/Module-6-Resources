from flask import Flask, render_template, redirect
from flask_migrate import Migrate

from .posts import posts, users
from app.routes.post_routes import post_routes
from app.config import Config
from app.models import db
from app.seeds import seed_commands

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)

app.cli.add_command(seed_commands)

app.register_blueprint(post_routes, url_prefix="/posts")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect('/posts/all', 302)

