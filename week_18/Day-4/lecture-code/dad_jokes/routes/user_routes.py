from flask import Blueprint

users_router = Blueprint('users', __name__)

@users_router.route('/')
def get_users():
    return "<h2>Users stuff will eventually be here</h2>"