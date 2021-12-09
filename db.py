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
        WHERE a.id IN (SELECT movie_id FROM movie_schedule as m where m.is_available ='1')
        order by id;
        """)
        mv = cursor.fetchall()

        mv_sch = {}
        for j in mv:
            id = j[1]
            id = convert.join_to_str(id)
            cursor.execute("""
            SELECT s.movie_id, s.cinema_id, s.day
            FROM movie_schedule as s LEFT OUTER JOIN movie as m 
            ON s.movie_id = m.id
            WHERE m.id = %s;
            """, (id,))
            sch = cursor.fetchall()
            mv_sch[j[0]] = sch
        
        #print(mv_sch)
        return mv_sch


    
    def get_cin(): 
        cursor.execute("""
        SELECT name, id FROM cinema as a
        WHERE a.id IN (SELECT cinema_id FROM movie_schedule as m where m.is_available ='1')
        order by id;
        """)
        cin = cursor.fetchall()
        #print(cin)

        mv_cin = {}
        for j in cin:
            id = j[1]
            id = convert.join_to_str(id)
            cursor.execute("""
            SELECT s.movie_id, s.cinema_id, s.day
            FROM movie_schedule as s LEFT OUTER JOIN cinema as c 
            ON s.cinema_id = c.id
            WHERE c.id = %s;
            """, (id,))
            cin = cursor.fetchall()
            mv_cin[j[0]] = cin
        
        #print(mv_cin)
        return mv_cin

    
    def get_dat():
        cursor.execute("""
        SELECT distinct(day) FROM movie_schedule as m where m.is_available ='1'
        order by day;
        """)
        dat = cursor.fetchall()
        str_dat = []
        for i in dat: 
            str_dat.append(i[0])
        return str_dat
    
    def get_sch():
        cursor.execute("""
        select m.id, m.movie_id, m.day, m.time_section_id, m.cinema_id, m.theater_floor, m.room_number, t.start_hr, mm.running_time from movie_schedule as m
        left outer join time_section as t on m.day = t.day and m.time_section_id = t.time_section_id
        left outer join movie as mm on m.movie_id = mm.id
        where m.is_available ='1';
        """)
        sch = cursor.fetchall()
        print(sch)
        return sch

class seatInfo: 
    def get_col_row(sch_id):
        cursor.execute("""
        select capacity_col, capacity_row
        FROM (SELECT m.cinema_id, m.theater_floor, m.room_number from movie_schedule as m where m.id =%s) as a
        JOIN theater as th ON a.cinema_id = th.cinema_id and a.theater_floor = th.floor and a.room_number = th.room_number;
        """, (sch_id,))
        capacity = cursor.fetchall()
        #print(capacity)
        return capacity

    def get_occupied(sch_id):
        cursor.execute("""
        select seat_col, seat_row 
        FROM ticket WHERE movie_schedule_id = %s
        """, (sch_id,))
        occupied = cursor.fetchall()
        print(occupied)
        return occupied
    
    def get_price(sch_id):
        cursor.execute("""
        select th.price FROM (SELECT m.cinema_id, m.theater_floor, m.room_number from movie_schedule as m where m.id =%s) as a
        JOIN theater as th ON a.cinema_id = th.cinema_id and a.theater_floor = th.floor and a.room_number = th.room_number;
        """, (sch_id,))
        price = cursor.fetchall()
        return price
        