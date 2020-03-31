from flask import Flask, render_template, url_for, request
from app import app

import requests, json

navbar = [
    {
        'itemText': 'HOME',
        'itemURL': '/'
    },
    {
        'itemText': 'ABOUT US',
        'itemURL': '/about'
    },
    {
        'itemText': 'EVENTS',
        'itemURL': '/events'
    },
    {
        'itemText': 'CONTACT',
        'itemURL': '/contact'
    }
]

@app.route('/')
def index():
    heading = "C'est Cheese on the Go"
    return render_template('index.html', heading=heading, navbar=navbar)

@app.route('/about')
def about():
    heading = "About"
    return render_template('about.html', heading=heading, navbar=navbar)

@app.route('/events')
def events():
    heading = "Events"
    return render_template('events.html', heading=heading, navbar=navbar)

@app.route('/contact')
def contact():
    heading = "Conact"
    return render_template('contact.html', heading=heading, navbar=navbar)