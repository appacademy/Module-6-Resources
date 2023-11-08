from flask import Flask, render_template, redirect 
from .config import Config
# from .posts import posts
from .routes.post_routes import posts 
from .routes.user_routes import users
from .models import db


app = Flask(__name__)
# print("main dudner init", __name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")



@app.route('/')
def index():
    """render the home page"""
    return render_template("index.html"), 202
    # return redirect("/another")
    # return {"important vals": ["one", "two", "three"]}


@app.route("/another")
def another_route():
    return "<h1>Another route</h1>"