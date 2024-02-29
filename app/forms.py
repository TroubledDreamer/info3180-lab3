from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

class contactform(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    text = TextAreaField('text', validators=[InputRequired()])
    email = TextAreaField('email', validators=[InputRequired()])
    subject = TextAreaField('subject', validators=[InputRequired()])

    

