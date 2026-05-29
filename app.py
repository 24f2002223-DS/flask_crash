from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "hellooo"

@app.route('/winner/<name>')
def winner(name):
    return "the winner is <h1>" + name + "</h1>"

@app.route("/singwinner")
def sing():
    return render_template('index.html')

@app.route("/namewithhtml/<name>")
def name(name):
    return render_template('name.html' , name = name)

@app.route("/styling/<name>")
def styke(name):
    return render_template("cssandimage.html" , name = name)

if(__name__ == "__main__"):
    app.run(debug = True)