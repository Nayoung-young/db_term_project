from flask import Flask
#from flask import render_template

from db import testQuery # python 파일에서 함수 가져오기 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/test')
def test():
    i = testQuery()
    return i

if __name__ == "__main__":
    app.run(debug=True)
