from flask import Blueprint, render_template

users_routes = Blueprint("users", __name__)

print("user routes", __name__)


@users_routes.route('/')
def get_users():
    return "<h1>User info coming soon...</h1>"