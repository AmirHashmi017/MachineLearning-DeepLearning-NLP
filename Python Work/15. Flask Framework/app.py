# Flask ia a python-based framework for webapps.
# The two most important components of Flask are:
# 1. WSGI (Web Server Gateway Interface): Applications are hosted on server like AWS,Apache and 
# user send requests to server. Server redirect requests to app and get response form app. The protocol used for
# Communication between server and Flask app is WSGI
# Ginga Template Engine: It is a web Template engine which is used for communication between web template 
# i.e web pages and Data Source which can be a Database,ML app or file. So it supports Dynamic web pages.
# It lets you write HTML templates that can dynamically render data from your Python backend.

# Basic Flask App Skeleton

from flask import Flask
# Make instance of Flask app i.e WSGI and spe ifying app entry point
app=Flask(__name__)

# Define app routes using decorators
@app.route('/')
def Welcome():
    return "Welcome to my Flask app Home Page."
@app.route('/index')
def idx():
    return "Welcome to index page"

if __name__=="__main__":
    # Run the flask app
    app.run(debug=True)
    # This debug=True reloads appication when we change in cide like live preview
