from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    #return "<p>Hello and welcome to Time-Hopping Travel & Cafe Experience App!</p>"
    return render_template("hey.html")
