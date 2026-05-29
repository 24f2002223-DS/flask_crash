from flask import Flask , render_template , redirect , url_for , request
app = Flask(__name__)
@app.route('/')
def home():
    return redirect('/login')

@app.route ( '/login', methods = ['POST' , 'GET'] )
def login():
    if request.method == 'POST':
        name = request.form['uid']
        return redirect(url_for('welcome' , user = name ))
    else :
        return render_template('login.html')
    
@app.route('/welcome/<user>')
def welcome(user):
    return render_template('welcome.html' , name = user)

if __name__ == '__main__' :
    app.run(debug = True)