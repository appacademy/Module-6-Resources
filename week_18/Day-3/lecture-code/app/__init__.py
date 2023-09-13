from flask import Flask, render_template, redirect 
from .config import Config
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db

app = Flask(__name__)
# print(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users)


@app.route("/")
def index():
    """return the index page view"""
    # return "<h1>Welcome to Patchstagram!</h1>"
    return render_template("index.html")
    # return redirect("/another")


@app.route("/another")
def another_route():
    return "<h2>This is another route!!!</h2>"

