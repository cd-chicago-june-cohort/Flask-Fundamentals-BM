from flask import Flask, render_template, request, redirect, session, jsonify
import random

app = Flask (__name__)
app.secret_key = "c2a1dfa3a243fa4e2eb035427f7af562" 

@app.route('/')
def index():
    if 'randnum' not in session:
        session['randnum'] = random.randrange(1,101)
    print str(session['randnum']) + " Is the number"
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = int(request.form['guess'])
   
    if session['guess'] < session['randnum']:
        print str(session['guess']) + " is TOO LOW"
        return render_template('guess.html', guessed_num = str(session['guess']) + ' is Too Low!')

    elif session['guess'] > session['randnum']:
        print str(session['guess']) + " is TOO HIGH"
        return render_template('guess.html', guessed_num = str(session['guess']) + ' is Too High!')

    elif session['guess'] == session['randnum']:
        print "YOU GUESSED IT"
        answer = str(session['guess']) + " is right!"
        return render_template('winner.html', guessed_num = str(session['guess']) + ' IS RIGHT!')

@app.route('/winner')
def winner ():
    session.clear()
    return redirect('/')

app.run(debug=True)