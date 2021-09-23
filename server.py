from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def principal():
    return 'Hola Mundo!'

@app.route('/dojo', methods=['GET'])
def dojo():
    return 'Dojo!'

@app.route('/say/<name>', methods=['GET'])
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>', methods=['GET'])
def repeat(num, word):
        text=f"<h3>{word}</h3>"
        return text*num

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)