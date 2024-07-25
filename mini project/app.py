from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
    "apiKey": "AIzaSyD7_wx_T9MgF-CMwb44tJpRflkIoIYvKJI",
    "authDomain": "mini-project-eecd3.firebaseapp.com",
    "projectId": "mini-project-eecd3",
    "storageBucket": "mini-project-eecd3.appspot.com",
    "messagingSenderId": "891050562936",
    "appId": "1:891050562936:web:d2a9166d9fac459114648d",
    "databaseURL": "https://mini-project-eecd3-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/')
def home():
    name = session.get('name', 'guest')
    signed_in = session.get('signed', False)
    return render_template("home.html", is_signed=signed_in, name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['name'] = db.child("Users").child(user['localId']).get().val()['name']
            session['signed'] = True
            return redirect(url_for('home'))
        except:
            return "Login error"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            db.child("Users").child(user['localId']).set({"name": name})
            session['name'] = name
            return redirect(url_for('home'))
        except:
            return "Signup error"
    return render_template('signup.html')

@app.route('/RPC', methods=['GET', 'POST'])
def RPC():
    return render_template('game.html')
@app.route('/game')

@app.route('/logout', methods=['POST'])
def logout():
    session["user"] = None
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
