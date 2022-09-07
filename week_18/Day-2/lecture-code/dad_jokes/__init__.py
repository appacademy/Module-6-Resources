from flask import Flask, render_template, redirect 
from .config import Config 
from .db_jokes import jokes
from random import choice
from .routes.jokes_routes import jokes_router
from .routes.user_routes import user_router


app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(jokes_router)
app.register_blueprint(user_router, url_prefix="/users")



@app.route('/')
def index():
    # this is where you would do DB stuff
    # jokes = Joke.query.all()
    joke = choice(jokes)
    print(joke)
    return render_template("index.html", joke=joke)
    # return redirect("/jokes/all", 302)





