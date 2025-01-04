from flask import Flask,render_template,request

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.

'''

##WSGI Application
app= Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html")

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name} welcome to my website. You are getting this response via post method'
    return render_template('form.html')

@app.route("/Submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello{name} welcome to my website. You are getting this response via post method'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)