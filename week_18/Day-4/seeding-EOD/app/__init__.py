from flask import Flask, render_template, redirect
from .config import Config
from .routes.post_routes import post_routes
from .routes.user_routes import user_routes
from .models import db
from flask_migrate import Migrate
from .seeds import seed_commands


app = Flask(__name__)
# print(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.cli.add_command(seed_commands)

app.register_blueprint(post_routes, url_prefix="/posts")
app.register_blueprint(user_routes, url_prefix="/users")

@app.route("/")
def index():
    """Landing page for our Patchstagram app"""
    # query for data
    # any other python logic we want
    print("I'm in the index route!!!!")
    return render_template("index.html")
    # return {"key": "some values"}


# @app.route("/all")
# def get_all_posts():
#     """Query for all posts and render a template displaying them"""
#     # posts = Post.query.all()
#     # return redirect("/")
#     return render_template("feed.html", posts=posts)


# @app.route("/<int:id>")
# def get_post_by_id(id):
#     # one_posr = Post.query.get(id)
#     one_post = [post for post in posts if post["id"] == id]
#     print(one_post)
#     return render_template("feed.html", posts=one_post)