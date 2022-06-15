from flask import Flask, render_template, redirect 
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_router
from .routes.user_routes import users_router
from .models.db import db, Joke



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(jokes_router) #/jokes
app.register_blueprint(users_router, url_prefix="/users")



@app.route('/')
def index():
    jokes = Joke.query.all()
    print(jokes)
    joke = choice(jokes)
    print(joke)
    return render_template("index.html", joke=joke)
    # return redirect("/another", 302)


# @app.route('/all')
# def all_jokes():
#     return render_template("all_jokes.html", jokes=jokes)


@app.route('/another')
def another_route():
    return "<h1>This is a totally different route!</h1>"