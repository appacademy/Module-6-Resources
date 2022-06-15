from flask import Blueprint

users_router = Blueprint('users', __name__)


@users_router.route('/')
def get_users():
    return "<h2>This is where we would see some users</h2>"