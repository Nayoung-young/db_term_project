from flask import Flask, render_template, request, redirect, session, url_for
from db import * # python 파일에서 함수 가져오기 

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('login.html')

@app.route('/movie', methods=['POST', 'GET'])
def movie_home():
    if request.method == 'POST':
        print(request.form)
        email = request.form['email']
        pwd = request.form['pwd']
        # get name 
        name = memberInfo.get_name(email, pwd)
        if name == None: 
            return "<h1>cannot find your information.</h1>back to <a href='/'>login</a>"
        else: pass
    else: 
        return '<h1>you cannot access this page without login</h1>'
    
    movies = movieInfo.get_movie()
    cinemas = ['1', '2']
    dates = ['1', '2']
    theaters = ['1', '2']

    return render_template('movie.html', 
        name=name, movies=movies, cinemas=cinemas, dates=dates, theaters=theaters)





if __name__ == "__main__":
    app.run(debug=True)
