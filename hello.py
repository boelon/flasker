from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

#Create a form class
class NamerForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


#Route decorator
@app.route('/')
#def index():
#   return "<h1>Hello World!</h1>"

def index():
    first_name="John"
    stuff = "This is <strong>bold</strong> text."
    flash("Welcome To Our Website!")
    title = "bob the blog builder"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           title=title,
                           favorite_pizza=favorite_pizza)

#localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


#Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")

    return render_template('name.html',
                           name = name,
                           form = form)