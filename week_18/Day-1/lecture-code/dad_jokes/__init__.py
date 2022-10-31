from flask import Flask, render_template
from .config import Config
from .db_jokes import jokes
from random import choice

app = Flask(__name__)

app.config.from_object(Config)


def get_all_jokes():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute(
            """
            SELECT *
            FROM jokes;
            """
        )
        results = curs.fetchone()
        print(curs)
        return results


@app.route('/')
def index():
    # jokes = Joke.query.all()
    joke = choice(jokes)
    return render_template("index.html", joke=joke)



@app.route('/all')
def get_all_jokes():
    # jokes = Joke.query.all()
    jokes = get_all_jokes()
    return render_template("all_jokes.html", jokes=jokes)



@app.route('/<int:id>')
def get_joke_by_id(id):
    print(id)
    # joke = Joke.query.get(id)
    one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke with that ID"
    return render_template("all_jokes.html", jokes=[one_joke])
