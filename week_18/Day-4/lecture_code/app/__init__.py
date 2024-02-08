from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from app.config import Config
# from .posts import posts, users
from .routes import user_routes, post_routes
from .models import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

Migrate(app, db)

app.register_blueprint(user_routes)
app.register_blueprint(post_routes, url_prefix="/posts")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")   

@app.route("/home")
def home():
    return redirect(url_for("index"), 302)

