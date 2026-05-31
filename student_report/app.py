from flask import Flask , render_template , redirect , request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('form.html')

@app.route('/report' , methods = ['POST' , 'GET'])
def report():
    if(request.method == 'POST'):
        report = request.form
        return render_template('table.html',report = report)
    return render_template('form.html')




if __name__ == '__main__' : 
    app.run(debug = True)