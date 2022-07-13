from flask import Flask, render_template, redirect
from dad_jokes.config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_router
from .routes.user_routes import users_router
from .models.db import db, Joke

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(jokes_router)
app.register_blueprint(users_router, url_prefix="/users")


@app.route('/')
def index():
    jokes = Joke.query.all()
    joke = choice(jokes)
    print("Here is our joke...", joke.to_dict())
    return render_template("index.html", joke=joke)
    # return redirect("/another", 302)


# @app.route('/all')
# def all_jokes():
#     return render_template("all_jokes.html", jokes=jokes)


@app.route('/another')
def another_route(): 
    return "<h1>This is another route, yay!</h1>"