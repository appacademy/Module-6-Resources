from flask import Flask, render_template, redirect
from .config import Config
# from .posts import posts as seed_posts
from .routes.post_routes import posts 
from .routes.user_routes import users
from .models import db
from flask_migrate import Migrate 
from .seeds import seed_commands
from flask_wtf.csrf import generate_csrf
import os 

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
app.cli.add_command(seed_commands)
app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")

# print(__name__)





@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


# @app.route("/")
# def index():
#     """renders the home page of our app"""
#     # query the DB
#     # return "<h1>Hello Programmers!</h1>"
#     return render_template("index.html")
#     # return redirect("/another")


# @app.route("/another")
# def another_route():
#     return "<h2>This is another route!!!</h2>"



# @app.route("/all")
# def get_all_posts():   
#     """gat all of the posts that exist and display them in a feed""" 
#     # query the DB for all posts
#     # all_posts = Post.query.all()
#     return render_template("feed.html", posts=posts)


# @app.route("/<int:id>")
# def get_post_by_id(id):
#     """display a single post by its id"""
#     # one_post = Post.query.get(id)
#     one_post = [post for post in posts if post["id"] == id]
#     print(one_post)
#     return render_template("feed.html", posts=one_post)


