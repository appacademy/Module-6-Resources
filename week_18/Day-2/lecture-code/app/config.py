import os



class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # more stuff to come like DB URL