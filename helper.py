from flask import Flask, session, render_template, request, abort, redirect, url_for
from weather import *
def fo(name):
    return 'Fuck off %s' %name 

def index(name=None):
    data = geo()
    return render_template('index.html',geo=data)
    