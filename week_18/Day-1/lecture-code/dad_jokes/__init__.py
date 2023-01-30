from flask import Flask, render_template  
from .config import Config
from .db_jokes import jokes
from random import choice

app = Flask(__name__)
app.config.from_object(Config)



# print(__name__)
@app.route("/")
def index():
    """Home route, will display a random joke"""
    joke = choice(jokes)
    print(joke)
    return render_template("index.html", joke=joke)




@app.route("/all")
def get_all_jokes():
    """Route to return and display all the jokes we have"""
    # all_joke = Joke.query.all()
    return render_template("all-jokes.html", jokes=jokes)



@app.route("/<int:id>")
def get_joke_by_id(id):
    print(id)
    one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke"
    return render_template("all-jokes.html", jokes=[one_joke])


