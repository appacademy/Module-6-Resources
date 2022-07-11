import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # add more private environment variables here