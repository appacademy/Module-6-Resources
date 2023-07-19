import os


class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  # do nut use this unless you're debugging a specific issue
  # SQLALCHEMY_ECHO = False