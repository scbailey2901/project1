from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField

class CreateForm(FlaskForm):
    propertyTitle=StringField('Property Title', validators=[InputRequired()])
    description=TextAreaField("Description", validators=[InputRequired()])
    numofrooms=StringField('No. of Rooms', validators=[InputRequired()])
    numofbathrooms = StringField("No. of Bathrooms", validators=[InputRequired()])
    price=StringField("Price", validators=[InputRequired()])
    propertytype=SelectField("Property Type", choices=[('1','Home'), ('2','Apartment')])
    location = StringField("Location", validators=[InputRequired()])
    photo=FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Images only!")])