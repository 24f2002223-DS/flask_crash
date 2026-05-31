from flask import Flask ,  redirect,render_template, request , session , url_for
app = Flask(__name__)
app.secret_key = 'aagurudhprasadya'

@app.route('/',methods = ['POST','GET'])
def entry():
    if(request.method == 'POST'):
        name = request.form['name']
        session['name'] = name 
        return redirect(url_for('dashboard'))
    return render_template('entry.html')

@app.route('/dashboard')
def dashboard():
    if 'name' not in session:
        return redirect('/')
    else:
        name = session.get('name')
        return render_template('dashboard.html' , name = name)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
