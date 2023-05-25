from flask import Flask, render_template, redirect, url_for, flash  
from .config import Config
from .routes.post_routes import posts
from .routes.user_routes import users
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_user, logout_user 
from .forms import LoginForm, LogoutForm, SignUpForm 


app = Flask(__name__)
# print(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(posts, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")

login = LoginManager(app)
login.login_view = "index"


@login.user_loader
def load_user(id):
    user = User.query.get(int(id))
    print(user, "inside user loader")
    return user


@app.route('/', methods=["GET", "POST"])
def index():
    """renders the site home page"""
    # if the user is logged in/authenticated they can just go back to the feed
    if current_user.is_authenticated:
        return redirect("/posts/all")

    form = LoginForm()

    if form.validate_on_submit():
        print(form.data["password"])
        user = User.query.filter(User.username == form.data["username"]).first()
        print(user)

        if not user or not user.check_password(form.data["password"]):
            flash('Login in failed 😢')
            # flashing docs https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/
            return redirect(url_for(".index"))
        
        login_user(user)
        print(current_user)
        return redirect("/posts/all")

    return render_template("index.html", form=form, messages=None)
    # return redirect("/another")


@app.route('/logout', methods=["POST"])
def logout():
    form = LogoutForm()

    if form.validate_on_submit():
        print(current_user, "before logout")
        logging_out_username = current_user.username 
        logout_user()
        flash(f"User: {logging_out_username} was logged out...")
        print(current_user, "after logout")
        return redirect("/")

    if form.errors:
        print(form.errors)
        return redirect("/posts/all")
    

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        new_user = User(
            username = form.data["username"],
            email = form.data["email"],
            password = form.data["password"],
            profile_pic = form.data["profile_pic"]  ,
            bio= form.data["bio"] ,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template(
            "signup.html", 
            form=form, 
            errors=form.errors
        )

    return render_template("signup.html", form=form, errors=None)


# @app.route('/another')
# def another_route():
#     return "<h2>This is totally another route!!</h2>"




