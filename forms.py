# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

class AddForm(FlaskForm):

    name = StringField('name of puppy: ')
    submit = SubmitField('Add puppy')

class DelForm(FlaskForm):
    id = IntegerField("ID Number of puppy ot remove: ")
    submit = SubmitField('Remove Puppy')

