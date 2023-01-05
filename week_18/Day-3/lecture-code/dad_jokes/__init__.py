from flask import Flask, render_template, redirect
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.joke_routes import jokes_router
from .routes.user_routes import users_routes
from .models import db, Joke

app = Flask(__name__)
app.config.from_object(Config)
# print("in dunder init", __name__)
db.init_app(app)

app.register_blueprint(jokes_router)
app.register_blueprint(users_routes, url_prefix="/users")



@app.route('/')
def index():
    """
    Landing page that returns a single random joke
    """
    jokes = Joke.query.all()
    # print([joke.to_dict() for joke in jokes])
    joke = choice(jokes)
    # response = joke.to_dict()
    # print(response)
    # return response
    return render_template('index.html', joke=joke, title="Dad Jokes")
    # return redirect("/another", 302)



@app.route("/another")
def redirected():
    return "<h1>We totally got redirected!</h1>"



# @app.route('/all')
# def all_jokes():
#     """
#     Returns all jokes in database
#     """
#     # jokes = Joke.query.all()
#     return render_template('all_jokes.html', jokes=jokes)


# @app.route('/<int:id>')
# def one_joke(id):
#     # one_joke = Joke.query.get(id)
#     one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke with that ID"
#     return render_template('all_jokes.html', jokes=[one_joke])