from flask import Flask, render_template, redirect
from flask_migrate import Migrate
# need to import seed commands from seeds folders
from .seeds import seed_commands
from .models import db
from .config import Config
from .routes.post_routes import posts
from .routes.user_routes import users


app = Flask(__name__)


app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

# Need to add the seed commands to our app
app.cli.add_command(seed_commands)

app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")


@app.route("/")
def index():
    """renders the home page"""
    return render_template("index.html")
    # return redirect("/another", 304)


@app.route("/another")
def another_route():
    return "<h1>This is an entirely different route!</h1>"

