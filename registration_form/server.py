from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')

 
app = Flask (__name__)

app.secret_key = "d0d879716b1552d4741ac855864e5c97"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    fname=request.form['first_name']
    lname=request.form['last_name']
    password=request.form['password']
    pass_conf=request.form['pass_conf']
    email=request.form['email']
    

    if len(request.form['first_name']) < 1:
        flash("Tell us your name.")
        return redirect('/')

    if not NAME_REGEX.match(request.form['first_name']):
        flash("That's not a real name.  If it is, our apologies.")
        return redirect('/')

    if len(request.form['last_name']) < 1:
        flash("Tell us your name.")
        return redirect('/')

    if not NAME_REGEX.match(request.form['last_name']):
        flash("That's not a real last name.  If it is, our apologies.")
        return redirect('/')

    if len(request.form['password']) < 8:
        flash("Password must be at least 9 characters long.")
        return redirect('/')        

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email. Try again, pal.")
        return redirect('/')

    if request.form['password'] != (request.form['pass_conf']):
        flash("Passwords must match.")
        return redirect('/')

    else:
        flash("success")
        return redirect('/')

    




app.run(debug=True)