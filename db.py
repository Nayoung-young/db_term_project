import psycopg2

db = psycopg2.connect("""
    host = localhost dbname=movies user=postgres password=0130 port=5432
    """)
cursor = db.cursor()

class convert:
    def tup_to_str(tup):
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
            return convert.tup_to_str(name)

class movieInfo:
    def get_mv():
        cursor.execute("""
        SELECT title FROM movie;
        """)
        movies = cursor.fetchall()
        str_mv = []
        for i in movies: 
            i = convert.tup_to_str(i)
            str_mv.append(i)
        #print(movies)
        return str_mv
    
    def get_cin(): 
        cursor.execute("""
        SELECT name FROM cinema;
        """)
        cin = cursor.fetchall()
        str_cin = []
        for i in cin: 
            i = convert.tup_to_str(i)
            str_cin.append(i)
        return str_cin
    
    def get_dat():
        cursor.execute("""
        SELECT distinct(day) FROM time_section;
        """)
        dat = cursor.fetchall()
        str_dat = []
        for i in dat: 
            str_dat.append(i[0])
        return str_dat
    
    

# def testQuery(): 
#     cursor.execute("SELECT * FROM instructor;")
#     return (cursor.fetchone()[1])

