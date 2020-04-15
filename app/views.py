from flask import Flask, render_template, url_for, request
from app import app
from google.oauth2 import service_account
#from apiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow

import requests, json
import googleapiclient.discovery 



topNavbar = [
    {
        'itemText': 'Facebook',
        'itemURL': 'https://www.facebook.com/cestcheeseonthego/'
    },
    {
        'itemText': 'Instagram',
        'itemURL': 'https://www.instagram.com/cestcheese.onthego/?hl=en' 
    }

]

bottomNavbar = [
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
    },

]

@app.route('/')
def index():
    heading = "C'est Cheese on the Go"
    return render_template('index.html', heading=heading, bottomNavbar=bottomNavbar, topNavbar=topNavbar)

@app.route('/about')
def about():
    heading = "About"
    return render_template('about.html', heading=heading, bottomNavbar=bottomNavbar, topNavbar=topNavbar)

@app.route('/events')
def events():
    heading = "Events"
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = 'app\cestcheese-36586cb857a8.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    import googleapiclient.discovery

    calendar = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    response = calendar.events().list(calendarId='03pglsplgu7kl5875em5r57cec@group.calendar.google.com', maxResults=10, timeMin='2020-01-01T10:00:00-07:00').execute()
    
    return render_template('events.html', heading=heading, bottomNavbar=bottomNavbar, topNavbar=topNavbar, events=response)

@app.route('/contact')
def contact():
    heading = "Contact"
    return render_template('contact.html', heading=heading, bottomNavbar=bottomNavbar, topNavbar=topNavbar)