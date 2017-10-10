from flask import Flask, session, render_template, request, abort, redirect, url_for, send_from_directory
from weather import *
from helper import *
app = Flask(__name__, static_url_path='/static')

#Just for kicks
@app.route('/fo/<name>')
def faos(name):
    return fo(name)
    

#Index
@app.route('/')
def hello(name=None):
    return index(name) 

@app.route('/weather')
def temp():
    return weather()
