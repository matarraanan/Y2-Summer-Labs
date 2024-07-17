from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        BM = request.form['BD']
        return redirect(url_for('fort', BM=BM))

@app.route('/fortune/<BM>')
def fort(BM):
   BM_int = int(BM)
   num = BM_int % 10
   forts = ["become a cat", "become a dog", "become a horse", "become a duck", "become a buck", 
                 "become a chef", "die", "never die", "be happy", "be sad"]
   ran = forts[num]
    
   return render_template("fortune.html", rand=ran)

if __name__ == '__main__':
    app.run(debug=True)
