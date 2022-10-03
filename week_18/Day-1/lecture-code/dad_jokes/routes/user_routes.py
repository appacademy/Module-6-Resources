from flask import Blueprint


user_router = Blueprint('users', __name__)


@user_router.route('/')
def get_users():
    return "<h2>This is where we will one day see users</h2>"