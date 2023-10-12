from flask import Flask, render_template, redirect
from .config import Config
# from .posts import posts
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db
from flask_migrate import Migrate


app = Flask(__name__)
# print(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)


app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")



@app.route("/")
def index():
    """home route will return the landing page"""
    # Query
    return render_template("index.html")
    # return redirect("/another")


# @app.route("/another")
# def another_route():
#     return "<h1>This is totally a different route!</h1>" 



@app.route("/all")
def get_all_posts():
    """get all the posts and return them """
    # all_post = Post.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    """return a single post by the id passed to the route"""
    # one_post = Post.query.get(id)
    one_post = [post for post in posts if post["id"] == id ]
    print(one_post)
    return render_template("feed.html", posts=one_post )

