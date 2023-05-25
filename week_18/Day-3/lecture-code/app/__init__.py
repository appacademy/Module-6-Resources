from flask import Flask, render_template, redirect
from .config import Config
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db


app = Flask(__name__)
print(__name__, "in the main __init__")

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")


@app.route("/")
def index():
    """Landing page"""
    # Query the DB
    # return "<h1>Welcome to our flask server!</h1>"
    return render_template("index.html")
    # return redirect("/another")


@app.route("/another")
def another():
    return "<h2>This is another route!!!</h2>"
