from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def root_page ():
    return render_template('index.html')



@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')


@app.route('/dojos/new')
def dojos ():
    return render_template('dojos.html')

@app.route('/dojos/new', methods=['POST'])
def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   print firstname
   print lastname
   # redirects back to the '/' route
   return redirect('/')


app.run(debug=True)