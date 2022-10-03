from flask import Flask, render_template
from .config import Config
from .db_jokes import jokes
from random import choice
from .routes.joke_routes import joke_router
from .routes.user_routes import user_router


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(joke_router)
app.register_blueprint(user_router, url_prefix="/users")
# print(__name__)


@app.route('/')
def index():
    joke = choice(jokes)
    # eventually we will query our DB  jokes = Joke.query.all()
    print(joke)
    return render_template("index.html", joke=joke, title='Dad Jokes')



# @app.route('/all')
# def all_jokes():
#     # eventually we will query our DB  jokes = Joke.query.all()
#     return render_template("all_jokes.html", jokes=jokes)
