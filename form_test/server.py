from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template('index.html', name = 'Bald Mike')
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users/<name>')
def show_user_profile(name):
    print name
    return render_template("users.html")

app.run(debug=True) # run our server