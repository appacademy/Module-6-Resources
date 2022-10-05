from flask import Flask, render_template, redirect
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import joke_router
from .routes.user_routes import user_router
from .models import db, Joke


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(joke_router)
app.register_blueprint(user_router, url_prefix="/users")



@app.route('/')
def index():
    jokes = Joke.query.all()
    joke = choice(jokes)

    response = joke.to_dict()
    print(response)
    return render_template("index.html", joke=joke, title='Dad Jokes')
    # return response 


@app.route("/another")
def sample_redirect():
    return "<h1>This is a whole new route!</h1>"


# @app.route('/all')
# def all_jokes():
#     # eventually we will query our DB  jokes = Joke.query.all()
#     return render_template("all_jokes.html", jokes=jokes)
