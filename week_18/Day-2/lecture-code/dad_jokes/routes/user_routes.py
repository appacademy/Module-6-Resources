from flask import Blueprint


users_router = Blueprint('users', __name__)


@users_router.route('/')
def get_user():
    return "<h2>This is where you would find some users...</h2>"