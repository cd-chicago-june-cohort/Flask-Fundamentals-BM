from flask import Flask, render_template, request, redirect, session, jsonify
import random
from datetime import datetime

app = Flask (__name__)
app.secret_key = "c2a1dfa3a243fa4e2eb035427f7af562" 

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money ():
    print "PROCESS"

    if request.form['building']=='farm':
        print "farm"
        session['newgold'] = random.randrange(10,21)
        session['gold'] += session['newgold']
        gold = session['gold']
        print gold
        activities=session['activities']
        activities.insert(0,"You just farmed your way to " + str(session['newgold']) +  " gold at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        session['activities']=activities
        print activities
        return redirect('/')

    elif request.form['building']=='cave':
        print "cave"
        session['newgold'] = random.randrange(5,11)
        session['gold'] += session['newgold']
        gold = session['gold']
        print gold
        activities=session['activities']
        activities.insert(0,"You just found " + str(session['newgold']) + " Gold in a cave at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        session['activities']=activities
        return redirect('/')

    elif request.form['building']=='house':
        print "house"
        session['newgold'] = random.randrange(5,11)
        session['gold'] += session['newgold']
        gold = session['gold']
        print gold
        activities=session['activities']
        activities.insert(0,"A house fell on you, collect " + str(session['newgold']) + " Gold at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        session['activities']=activities
        return redirect('/')

    elif request.form['building']=='casino':
        print "casino"
        session['newgold'] = random.randrange(-50,50)
        session['gold'] += session['newgold']
        gold = session['gold']
        print gold
        activities=session['activities']
        if session['newgold'] < 0:
            activities.insert(0,"You just lost " + str(session['newgold']) + " Gold at the Casino at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else: 
            activities.insert(0,"You just won " + str(session['newgold']) + " Gold at the Casino at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        session['activities']=activities
        if gold < 0:
            activities.insert(0,"You outta cash, FOOL.")
            return redirect('/reset')
        return redirect('/')




@app.route('/reset')
def reset ():
    session.clear()
    return redirect('/')

app.run(debug=True)


# , gold=(session['gold']), activities=(session['activities'])