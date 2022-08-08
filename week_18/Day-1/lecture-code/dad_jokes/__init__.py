from flask import Flask, render_template
from .config import Config
from .db_jokes import jokes
from random import choice

app = Flask(__name__)
app.config.from_object(Config)

print("This is what name looks like", __name__)


@app.route('/')
def index():
    joke = choice(jokes)
    print(joke)
    return render_template('index.html', joke=joke)


@app.route('/all')
def all_jokes():
    # Eventually we will query our DB for the jokes here
    return render_template('all_jokes.html', jokes=jokes)    
