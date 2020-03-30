from flask import Flask, render_template
from app import app


@app.route('/')
def index():
    heading = "C'est Cheese on the Go"
    return render_template('index.html', heading=heading)
