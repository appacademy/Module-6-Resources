from flask import Flask, render_template 
from .config import Config
from .db_jokes import jokes
from random import choice

app = Flask(__name__)
app.config.from_object(Config)
# print(__name__)


@app.route('/')
def index():
    joke = choice(jokes)
    # joke = Joke.query.all()
    
    return render_template("index.html", joke=joke)


@app.route("/all")
def all_jokes():
    return render_template("all_jokes.html", jokes=jokes)


@app.route("/<int:id>")
def joke_by_id(id):
    print(id)
    one_joke = jokes[id - 1]
    return render_template("all_jokes.html", jokes=[one_joke])