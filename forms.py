from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL, NumberRange

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species",choices = ["cats", "dogs", "porcupines"])
    photo_url = StringField("Photo URL",validators=[URL()])
    age = IntegerField("Age", validators = [NumberRange(min=0,max=30)])
    notes = StringField("Notes")
    available = BooleanField("Available ?")


class PetForm(FlaskForm):
    photo_url = StringField("Photo URL",validators=[URL()])
    notes = StringField("Notes")
    available = BooleanField("Available ?")