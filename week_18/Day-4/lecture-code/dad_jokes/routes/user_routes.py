from flask import Blueprint, request
from ..models.db import User
from random import choice

users_router = Blueprint('users', __name__)


@users_router.route('/')
def get_user():
    
    # how to get the response info from a React Fetch call
    # data = request.json()

    if request.method == "GET":
        print("hey we got a get request!")

    print(data)
    users = User.query.all()
    # user = choice(users)
    response = [user.to_dict() for user in users]
    print(response)
    return { "users": response }