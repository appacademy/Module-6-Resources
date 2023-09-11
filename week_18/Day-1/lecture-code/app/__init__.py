from flask import Flask, render_template 
from .config import Config
from .posts import posts
from .forms.post import add4
# from .models.user import add6
# from .models.posts import add8
from .models import add10, add6, add8


app = Flask(__name__)
print(__name__)

print(add4(4))
print(add6(4))
print(add8(4))
print(add10(4))

app.config.from_object(Config)


@app.route("/")
def index():
    """return the index page view"""
    # return "<h1>Welcome to Patchstagram!</h1>"
    return render_template("index.html")


@app.route("/all")
def get_all_posts():
    """returns all posts"""
    # Query   posts = Posts.query.all()
    return render_template("feed.html", posts=posts)


@app.route("/<int:id>")
def get_post_by_id(id):
    """returns a single post by the given id provided as a route parameter"""
    # one_post = Posts.query.get(id)
    one_post = [ post for post in posts if post['id'] == id]
    return render_template("feed.html", posts=one_post)
