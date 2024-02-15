from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Congratulations! You just built your first Docker image!!!!</h1>\
                <h2>Then you created a container and served a flask app from inside!!!!</h2>"
