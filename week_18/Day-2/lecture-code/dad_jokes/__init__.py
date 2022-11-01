from flask import Flask, render_template, redirect
from .config import Config
from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_router
from .routes.user_routes import users_router


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(jokes_router)
app.register_blueprint(users_router, url_prefix="/users")



@app.route('/')
def index():
    # jokes = Joke.query.all()
    joke = choice(jokes)
    return render_template("index.html", joke=joke)
    # return redirect("/another", 302)


@app.route('/another')
def another_route():
    return "<h2>Totally different route</h2>"


