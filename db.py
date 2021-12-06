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
    def get_movie():
        cursor.execute("""
        SELECT age, title FROM movie;
        """)
        movies = cursor.fetchall()
        print(movies)
        return movies
    
    

# def testQuery(): 
#     cursor.execute("SELECT * FROM instructor;")
#     return (cursor.fetchone()[1])

