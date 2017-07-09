from flask import Flask, render_template, request, redirect, session, flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask (__name__)

app.secret_key = "2f25d49a3c53ff90e78a1584cee89353"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process_form():
    name=request.form['name']
    dojo=request.form['dojo']
    language=request.form['language']
    comment=request.form['comments']

    print name
    print dojo
    print language
    print comment

    if len(request.form['name']) < 1:
        flash("Please enter YOUR NAME")
        return redirect('/')

    if (request.form['dojo']) == 'null':
        flash("Please enter THE DOJO")
        return redirect('/')

    if (request.form['language']) == 'null':
        flash("Please pick a language")
        return redirect('/')
        
    else:
        return render_template('result.html', newname=name, newdojo=dojo, newlanguage=language, newcomment=comment)
    

# @app.route('/process', methods=['POST', 'GET'])
# def process_form():







# This validates that SOMETHING was entered into 'name' field
# @app.route('/process', methods=['POST'])
# def process():
#     if len(request.form['name']) < 1:
#         flash("Name cannot be empty!")
#     else:
#         flash("Success! Your name is {}".format(request.form['name']))
#     return redirect('/')



# This validates an email input
# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

# @app.route('/process', methods=['POST'])
# def submit():
#     if len(request.form['email']) < 1:
#         flash("Email cannot be blank!")
#     # else if email doesn't match regular expression display an "invalid email address" message
#     elif not EMAIL_REGEX.match(request.form['email']):
#         flash("Invalid Email Address")
#     else:
#         flash("Success!")
#     return redirect('/')






app.run(debug=True)