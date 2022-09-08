import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # define any other secret environment variables here
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False