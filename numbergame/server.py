from flask import Flask, render_template, request, redirect, session
import random

app = Flask (__name__)
app.secret_key = "c2a1dfa3a243fa4e2eb035427f7af562" 

randnum = random.randrange(1,101)

@app.route('/')
def index():
    print randnum

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    
    if session['guess']==randnum:
        print "YOU GUESSED IT"

    else:
        print "you made it to guess"
        print session['guess']
    
    return redirect('/')



app.run(debug=True)