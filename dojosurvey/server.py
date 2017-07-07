from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    name=request.form['name']
    dojo=request.form['dojo']
    language=request.form['language']
    comment=request.form['comments']

    print name
    print dojo
    print language
    print comment

    return render_template('result.html', newname=name, newdojo=dojo, newlanguage=language, newcomment=comment)

app.run(debug=True)