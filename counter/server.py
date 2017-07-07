from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
app.secret_key = "8f32dfc68a0047a8e8bf1960e7ce79a0"

@app.route('/')
def index():
    print session
    if 'clicker' in session:
        session['clicker'] += 1
    else: 
        session['clicker'] = 1
    return render_template('index.html')

@app.route('/twice')
def twice():
    session['clicker'] += 2
    print "TWICE"
    return render_template('index.html')    

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



app.run(debug=True)


