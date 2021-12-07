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
    
    movies = movieInfo.get_mv()
    cinemas = movieInfo.get_cin()
    dates = movieInfo.get_dat()

    return render_template('movie.html', 
        name=name, movies=movies, cinemas=cinemas, dates=dates)

@app.route('/movie/seats', methods=['POST', 'GET'])
def test():
    return 

@app.route('/myticket', methods=['POST', 'GET'])
def testt():
    return 

if __name__ == "__main__":
    app.run(debug=True)
