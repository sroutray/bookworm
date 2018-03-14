"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import render_template
from ourWebapp import app
from flask import request, redirect, url_for, render_template, flash
from werkzeug import secure_filename

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about',  methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        """Renders the about page."""
        return render_template(
            'about.html',
            title='Summariser',
            year=datetime.now().year,
            content=None
        )
    elif request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file uploaded')   # to be implemented in the page html layout
            return redirect(url_for('about'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_output = open(os.path.join(app.config['UPLOAD_FOLDER'], "output.txt"), "a+")
            file_input = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "r")
            #summarise_book(file_input, file_output)
            content = file_input.read()
		#f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "r")
        #os.system('rm ./files/output.txt')
        return render_template(
            'about.html',
            title='Summariser',
            year=datetime.now().year,
            content=content
        )
