from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to Dad Jokes!</h1>"