import psycopg2

db = psycopg2.connect("""
    host = localhost dbname=movies user=postgres password=0130 port=5432
    """)
cursor = db.cursor()

class convert:
    def join_to_str(tup):
        return ''.join(tup)

class memberInfo:
    def get_name(email, pwd):
        cursor.execute("""
            SELECT name FROM member where email = (%s) and password = (%s)
            """, (email, pwd))
        name = cursor.fetchone()
        if name is None: 
            return None
        else: 
            return convert.join_to_str(name)

class movieInfo:
    def get_mv():
        cursor.execute("""
        SELECT * FROM movie as a
        WHERE a.id IN (SELECT movie_id FROM movie_schedule);
        """)
        movies = cursor.fetchall()
        print(movies)
        return movies
    
    def get_cin(): 
        cursor.execute("""
        SELECT * FROM cinema as a
        WHERE a.id IN (SELECT cinema_id FROM movie_schedule);
        """)
        cin = cursor.fetchall()
        print(cin)
        return cin
    
    def get_dat():
        cursor.execute("""
        SELECT distinct(day) FROM movie_schedule
        order by day;
        """)
        dat = cursor.fetchall()
        str_dat = []
        for i in dat: 
            str_dat.append(i[0])
        return str_dat


