from flask import Flask
from dad_jokes.config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    print("Hey we hit the index route, yay!")
    return "<h1>Welcome to Dad Jokes!</h1>"