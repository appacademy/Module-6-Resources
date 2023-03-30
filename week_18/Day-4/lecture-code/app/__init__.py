from flask import Flask, render_template , redirect 
from .config import Config
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")


# print("in __init__", __name__)


@app.route("/")
def index():
    """renders the home page"""
    return render_template("index.html")
    # return redirect("/another")


@app.route("/another")
def another():
    return "<h2>This is another route!</h2>"






