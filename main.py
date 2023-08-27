from flask import Flask,  render_template, url_for, request
from flask import Flask, flash, request, redirect, url_for
import MyFunc_shingles
import MyFunc

app = Flask(__name__)


@app.route('/question', methods=['POST', 'GET'])
def question():
    if request.method == 'POST':
        data = request.get_json(force=True)
    return MyFunc_shingles.question(data["question"])


@app.route('/questiontwo', methods=['POST', 'GET'])
def questiontwo():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print("HIGHT")
    return MyFunc.question(data["question"])


@app.route('/')
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
