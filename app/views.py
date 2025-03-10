"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash,  send_from_directory
from werkzeug.utils import secure_filename
from app.forms import CreateForm
from app.models import PropertyProfile
from flask_migrate import Migrate




###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/properties/create', methods=['GET', 'POST'])
def addNewProperty():
    form=CreateForm()
    if request.method=="POST":       
        if form.validate_on_submit():
            propertyTitle=form.propertyTitle.data
            description= form.description.data
            numofrooms=form.numofrooms.data
            numofbathrooms=form.numofbathrooms.data
            price=form.price.data
            location = form.location.data
            propertytype=form.propertytype.data
            photo=form.photo.data
            filename= secure_filename(photo.filename)
            print(filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_property = PropertyProfile(propertyTitle=propertyTitle, propertyDescription=description, numofrooms=numofrooms, numofbathrooms=numofbathrooms, price=price, propertytype=propertytype, location=location, photo_path=filename)
            db.session.add(new_property)
            db.session.commit()
            flash('Property Added', 'success')
            return redirect(url_for("properties"))
        else:
            flash_errors(form)
    return render_template('createproperty.html', form=form)

@app.route('/properties')
def properties():
    properties = PropertyProfile.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def getProperty(propertyid):
    property = PropertyProfile.query.filter_by(id=propertyid).first()
    return render_template('property.html', property=property)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
