from flask import Flask, render_template, request, redirect, url_for, session as login_session

app = Flask(__name__)
app.secret_key = 'pass'  

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template("main.html")
    else:
        name = request.form['username']
        birthmonth = request.form['BD']  
        login_session['username'] = name  
        login_session['birthmonth'] = birthmonth  
        return redirect(url_for('home'))

@app.route('/home')
def home():
    name = login_session['username']
    birthmonth = login_session['birthmonth']
    
    if name is None or birthmonth is None:
        return redirect(url_for('main'))
    
    BD_int = int(birthmonth)
    if len(birthmonth) == 0 or len(birthmonth) > 2 or BD_int > 31:
        return render_template("fortune.html", rand="enter a normal day", title=name + ", enter your day in a correct format")
    else:    
        num = BD_int % 10
        forts = ["invalid input", "become a cat", "become a dog", "become a horse", "become a duck", "become a buck", 
                 "become a chef", "die", "never die", "be happy", "be sad"]
        ran = forts[num]
        login_session['fortune'] = ran 
        return render_template("home.html", name=name)

@app.route('/fortune')
def fortune():
    if 'fortune' in login_session:
        fortune = login_session['fortune']
        name = login_session['username']
        return render_template("fortune.html", rand=fortune, title="Hey," + name +" here's your fortune", name=name)
    else:
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
