from flask import Blueprint


users_routes = Blueprint('users', __name__)

print("in user bp", __name__)


@users_routes.route('/all')
def get_al_users():
    return "<h2>Here are all of our lovely users</h2>"