from flask import Flask, render_template, url_for
#from flaskr.db import get_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')