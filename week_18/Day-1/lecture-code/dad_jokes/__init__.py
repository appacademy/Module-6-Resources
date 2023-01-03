from flask import Flask, render_template
from .config import Config
from .db_jokes import jokes
from random import choice

app = Flask(__name__)
app.config.from_object(Config)
print(__name__)


@app.route('/')
def index():
    """
    Landing page that returns a single random joke
    """
    joke = choice(jokes)

    return render_template('index.html', joke=joke)


@app.route('/all')
def all_jokes():
    """
    Returns all jokes in database
    """
    # jokes = Joke.query.all()
    return render_template('all_jokes.html', jokes=jokes)


@app.route('/<int:id>')
def one_joke(id):
    # one_joke = Joke.query.get(id)
    one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke with that ID"
    return render_template('all_jokes.html', jokes=[one_joke])