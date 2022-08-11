from flask import Flask, render_template, redirect
from .config import Config
# from .db_jokes import jokes
from random import choice
from .routes.jokes_routes import jokes_router
from .routes.user_routes import users_router
from .models import db, Joke
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(jokes_router)
app.register_blueprint(users_router, url_prefix='/users')

# print("This is what name looks like", __name__)



@app.route('/')
def index():
    jokes = Joke.query.all()
    joke = choice(jokes)
    print(joke.to_dict())
    # print(joke.user)
    return render_template('index.html', joke=joke)




@app.route('/test')
def test_redirect():
    return redirect('/all', 302)