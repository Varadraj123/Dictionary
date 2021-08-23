from flask import Flask,request,render_template
from textblob import Word

app = Flask(__name__)  
  
@app.route('/')  
def customer():  
    return render_template('form.html')  
  
@app.route('/dictionary',methods = ['POST', 'GET'])  
def print_data():  
    if request.method == 'POST':  
        meaning= request.form.get("word")
        print(f'******************** Input word is :{meaning}:')
        result = Word(meaning).definitions
              
    return render_template("form.html",final_result = 'Meaning of your word is :\n{}'.format(result))  

if __name__ == '__main__':  
    app.run(debug = True)