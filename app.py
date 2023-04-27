from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from forms import AddPet, PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet'
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '<replace with a secret key>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)

with app.app_context():
    db.create_all()






@app.route('/')
def home():
    pets = Pet.query.all()
    form = AddPet()
    return render_template('base.html', pets = pets, form=form)

@app.route('/add', methods = ["GET", "Post"])
def add():
    form = AddPet()
    if form.validate_on_submit():
        new_pet = Pet(
        name = form.name.data,
        species = form.species.data,
        photo_url = form.photo_url.data,
        age = form.age.data,
        notes = form.notes.data,
        available = form.available.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} has been added")
        return(redirect('/'))
    else: 
        return render_template('pet-form.html', form = form)

@app.route('/pet/<int:id>', methods = ["Post","GET"])
def getPet(id):
    pet = Pet.query.get(id)
    pet_update = PetForm(obj=pet)
    if pet_update.validate_on_submit():
        pet.photo_url = pet_update.photo_url.data,
        pet.notes = pet_update.notes.data,
        pet.available = pet_update.available.data
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} has been added")
        return redirect("/")
    return render_template('pet.html', id = id, pet = pet, update = pet_update)

