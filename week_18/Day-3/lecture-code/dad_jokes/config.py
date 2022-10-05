import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # eventually store DB connection here too
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False