from flask import Flask, render_template, redirect  
from .config import Config
from .db_jokes import jokes
from random import choice
from .routes.joke_routes import joke_routes
from .routes.user_routes import user_routes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(joke_routes)
app.register_blueprint(user_routes, url_prefix="/users")


# print(__name__)
@app.route("/")
def index():
    """Home route, will display a random joke"""
    joke = choice(jokes)
    print(joke)
    # return redirect("/another", 302)
    return render_template("index.html", joke=joke)


@app.route("/another")
def another_route():
    return "<h1>This is another totally different route! </h1>"




