from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
    "apiKey": "AIzaSyAY6FWrbQKOFDLQahLl3B4tvhXbUEYnEgw",
    "authDomain": "auth-e78c4.firebaseapp.com",
    "projectId": "auth-e78c4",
    "storageBucket": "auth-e78c4.appspot.com",
    "messagingSenderId": "869098061082",
    "appId": "1:869098061082:web:4af3ee8511991ea0af00a3",
    "databaseURL": "https://auth-e78c4-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        username = request.form['username']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            user_data = {
                "full_name": full_name,
                "email": email,
                "username": username
            }
            db.child("Users").child(user['localId']).set(user_data)
            return redirect(url_for('home'))
        except:
            return "error"
    return render_template("signup.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('home'))
        except:
            return "error"
    return render_template("signin.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quote_text = request.form['quote']
        said_by = request.form['said_by']
        quote = {
            'text': quote_text,
            'said_by': said_by,
            'uid': session['user']['localId']
        }
        db.child("Quotes").push(quote)
        return redirect(url_for('thanks'))
    return render_template("home.html")

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/display')
def display():
    quotes = db.child("Quotes").get().val()
    return render_template("display.html", quotes=quotes)

@app.route('/signout', methods=['POST'])
def signout():
    session["user"] = None
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
