from flask import Flask, render_template, redirect 
from .config import Config 
from random import choice
from .routes.jokes_routes import jokes_router
from .routes.user_routes import user_router
from .models import db, Joke

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(jokes_router)
app.register_blueprint(user_router, url_prefix="/users")



@app.route('/')
def index():
    jokes = Joke.query.all()
    joke = choice(jokes)
    print(joke.to_dict())
    return render_template("index.html", joke=joke)
    # return redirect("/jokes/all", 302)
    # return joke.to_dict()





