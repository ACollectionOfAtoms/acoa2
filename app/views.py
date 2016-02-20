from flask import render_template, flash, redirect, url_for, session, request, g
from app import app

nav = 'home, projects, about'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')