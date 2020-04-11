from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired()])
  subject = StringField('Subject', validators=[DataRequired()])
  textarea = TextAreaField('Message', validators=[DataRequired()])
  submit = SubmitField('submit')