from flask import Flask ,  redirect,render_template, request , session , url_for , make_response
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
    name = session.get('name')
    message = request.args.get('message', 'do cookie operations !!')
    return render_template('dashboard.html', name=name, message=message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/cookie')
def sc():
    response = make_response(redirect(url_for('dashboard', message='setting cookie')))
    response.set_cookie('name', session.get('name'))
    return response

@app.route('/get_cookie')
def gc():
    val = request.cookies.get('name')
    message = val if val is not None else 'no cookie found'
    return redirect(url_for('dashboard', message=message))

@app.route('/remove_cookie')
def rc():
    response = make_response(redirect(url_for('dashboard', message='cookie removed')))
    response.delete_cookie('name')
    return response


if __name__ == '__main__':
    app.run(debug=True)
