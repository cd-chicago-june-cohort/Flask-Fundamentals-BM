from flask import Flask, render_template, request, redirect
 
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def show_ninjas():
    return render_template('ninja.html')
    print 'Showed Ninjas'

@app.route('/ninja/<color>')
def show_each (color):
    print color
    return render_template('which.html', pic=color)
   
app.run(debug=True)