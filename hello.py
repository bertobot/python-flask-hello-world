from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/bye")
def bye1():
    return "Goodbye World!"

@app.route("/bye/<name>")
def bye2(name):
    return "Goodbye {0}".format(name)

