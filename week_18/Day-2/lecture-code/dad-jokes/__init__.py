from flask import Flask, render_template, redirect 
from .config import Config
from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_routes
from .routes.user_routes import users_routes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(jokes_routes)
app.register_blueprint(users_routes, url_prefix="/users")


@app.route('/')
def index():
    joke = choice(jokes)
    # joke = Joke.query.all()
    return render_template("index.html", joke=joke)
    # return redirect('/another')


@app.route("/another")
def another_route():
    return "<h1> This is another route </h1>"