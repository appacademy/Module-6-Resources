from flask import Blueprint

user_router = Blueprint("users", __name__)


@user_router.route('/')
def get_user():
    return "<h2>This is where user info will be <h2>"