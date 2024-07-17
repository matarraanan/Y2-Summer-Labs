from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        BD = request.form['BD']
        return redirect(url_for('fort', BD=BD))

@app.route('/fortune/<BD>')
def fort(BD):
    try:
        if len(BD) == 0 or len(BD) > 2:
            return render_template("fortune.html", rand="enter a normal day", title="Bro, enter your day in a correct format")
        else:
            BD_int = int(BD)
            num = BD_int % 10
            forts = [0,"become a cat", "become a dog", "become a horse", "become a duck", "become a buck", 
                     "become a chef", "die", "never die", "be happy", "be sad"]
            ran = forts[num]
            return render_template("fortune.html", rand=ran, title="Hey, here's your fortune")
    except ValueError:
        return render_template("fortune.html", rand="enter a valid number", title="Invalid input")

if __name__ == '__main__':
    app.run(debug=True)
