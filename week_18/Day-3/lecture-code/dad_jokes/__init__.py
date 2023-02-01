from flask import Flask, render_template, redirect  
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import joke_routes
from .routes.user_routes import user_routes

from .models import db, Joke


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(joke_routes)
app.register_blueprint(user_routes, url_prefix="/users")


# print(__name__)
@app.route("/")
def index():
    """Home route, will display a random joke"""
    jokes = Joke.query.all()
    joke = choice(jokes)
    print(joke.to_dict())
    # return redirect("/another", 302)
    return render_template("index.html", joke=joke)
    # return joke.to_dict()


@app.route("/another")
def another_route():
    return "<h1>This is another totally different route! </h1>"




