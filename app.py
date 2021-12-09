from flask import Flask, render_template, request, redirect, session, url_for
from db import * # python 파일에서 함수 가져오기 

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('login.html')

@app.route('/movie', methods=['POST', 'GET'])
def movie_home():
    if request.method == 'POST':
        # print(request.form)
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
    mv_schs = movieInfo.get_sch() 

    return render_template('movie.html', email=email,
        name=name, movies=movies, cinemas=cinemas, dates=dates, mv_schs = mv_schs)

@app.route('/seats', methods=['POST', 'GET'])
def movie_seats():
    return render_template('seat.html')
    if request.method == 'POST': 
    # 앞에서 선택한 정보 받아서, 상영관 좌석 보여주기 
    # 이미 예약된 좌석은 다른 색으로 처리 
        return render_template('seat.html')

@app.route('/movie/seats/check', methods=['POST', 'GET'])
def movie_check():
    if request.method == 'POST': 
        # ticket table에 저장 후 확인 메시지 출력 
        return render_template('movie_check.html')

@app.route('/myticket', methods=['POST', 'GET'])
def show_ticket():
    return render_template('myticket.html')





if __name__ == "__main__":
    app.run(debug=True)
