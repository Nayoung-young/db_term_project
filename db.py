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
        SELECT title, id FROM movie as a
        WHERE a.id IN (SELECT movie_id FROM movie_schedule)
        order by id;
        """)
        mv = cursor.fetchall()

        mv_sch = {}
        for j in mv:
            id = j[1]
            id = convert.join_to_str(id)
            cursor.execute("""
            SELECT m.id, s.cinema_id, s.day
            FROM movie_schedule as s LEFT OUTER JOIN movie as m 
            ON s.movie_id = m.id
            WHERE m.id = %s;
            """, (id,))
            sch = cursor.fetchall()
            mv_sch[j[0]] = sch
        
        print(mv_sch)
        return mv_sch


    
    def get_cin(): 
        cursor.execute("""
        SELECT name, id FROM cinema as a
        WHERE a.id IN (SELECT cinema_id FROM movie_schedule)
        order by id;
        """)
        mv = cursor.fetchall()

        mv_cin = {}
        for j in mv:
            id = j[1]
            id = convert.join_to_str(id)
            cursor.execute("""
            SELECT m.id, s.cinema_id, s.day
            FROM movie_schedule as s LEFT OUTER JOIN cinema as m 
            ON s.cinema_id = m.id
            WHERE m.id = %s;
            """, (id,))
            cin = cursor.fetchall()
            mv_cin[j[0]] = cin
        
        print(mv_cin)
        return mv_cin

    
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


