from flask import Flask, render_template, request, redirect, session, flash, Markup

app = Flask (__name__)

app.secret_key = "d0d879716b1552d4741ac855864e5c97"

@app.route('/', methods=['POST', 'GET'])
def process_form():
    red=123
    blue=123
    green=123



    if request.method == ['POST']:

        red=request.form['red']
        blue=request.form['blue']
        green=request.form['blue']
        print ("red, green, blue")
    
        return render_template('/index.html', red=red, green=green, blue=blue)
        
    else:
        return render_template('/index.html')


    




app.run(debug=True)