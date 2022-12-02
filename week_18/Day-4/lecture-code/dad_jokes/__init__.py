from flask import Flask, render_template, redirect 
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_routes
from .routes.user_routes import users_routes
from .models import db, Joke
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(jokes_routes)
app.register_blueprint(users_routes, url_prefix="/users")


@app.route('/')
def index():
    jokes = Joke.query.all()
    # print(jokes)
    joke = choice(jokes)
    print(joke)
    print(joke.to_dict())
    return render_template("index.html", joke=joke)
    # return redirect('/another')
    # response = joke.to_dict()
    # print(response)
    # return response


@app.route("/another")
def another_route():
    return "<h1> This is another route </h1>"