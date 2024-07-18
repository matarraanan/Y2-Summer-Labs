from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
app = Flask(__name__)



@app.route('/',methods=['GET', 'POST    '])
def main():
    if request.method == ' GET':
        return render_template("main.html")
    else:
        name = request.form['username']
        passw = request.form['pass']
        birthmonth =         

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        BD = request.form['BD']
        return redirect(url_for('fort', BD=BD))

@app.route('/fortune/<BD>')
def fort(BD):
   BD_int = int(BD)
   if len(BD) == 0 or len(BD) > 2 or BD_int > 31:
      return render_template("fortune.html", rand="enter a normal day", title="Bro, enter your day in a correct format")
   else:    
      num = BD_int % 10
      forts = ["inavalid input","become a cat", "become a dog", "become a horse", "become a duck", "become a buck", 
                     "become a chef", "die", "never die", "be happy", "be sad"]
      ran = forts[num]
      return render_template("fortune.html", rand=ran, title="Hey, here's your fortune")
    



if __name__ == '__main__':
    app.run(debug=True)
