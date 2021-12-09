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
        password = request.form['password']
        # get name 
        name = memberInfo.get_name(email, password)
        if name == None: 
            return "<h1>cannot find your information.</h1>back to <a href='/'>login</a>"
        else: pass
    else: 
        return '<h1>you cannot access this page without login</h1>'
    
    movies = movieInfo.get_mv()
    cinemas = movieInfo.get_cin()
    dates = movieInfo.get_dat()
    mv_schs = movieInfo.get_sch() 

    return render_template('movie.html', email=email, password=password,
        name=name, movies=movies, cinemas=cinemas, dates=dates, mv_schs = mv_schs)

@app.route('/seats', methods=['POST', 'GET'])
def movie_seats():
    if request.method == 'POST': 
    # 앞에서 선택한 정보 받아서, 상영관 좌석 보여주기 
    # 이미 예약된 좌석은 다른 색으로 처리 
        print (request.form)
        email = request.form['email']
        password = request.form['password']

        sch_id = request.form['sch']
        name = memberInfo.get_name(email, password)
        # get_sch_info 

        # theater에서 col, row 수 
        
        capacity = seatInfo.get_col_row(sch_id) # [col, row]
        col = capacity[0][0]
        row = capacity[0][1]

        # ticket에서 예매 가능한 좌석 col, row 가져오기 
        capacity_occupied = seatInfo.get_occupied(sch_id)

        # theater 가격 정보 가져오기 
        price = seatInfo.get_price(sch_id)
        price = price[0][0]

        return render_template('seat.html', name=name, email=email, password=password, sch_id=sch_id, col=col, row=row, price=price)

@app.route('/seats_check', methods=['POST', 'GET'])
def movie_check():
    if request.method == 'POST': 
        # ticket table에 저장 후 확인 메시지 출력 
        return render_template('movie_check.html')

@app.route('/myticket', methods=['POST', 'GET'])
def show_ticket():
    return render_template('myticket.html')





if __name__ == "__main__":
    app.run(debug=True)
