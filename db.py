import psycopg2

db = psycopg2.connect(host='localhost', 
    dbname='movies', user='postgres', password='0130', port='5432')
cursor = db.cursor()

class memberInfo:
    def get_name(email):
        email = '\''+email+'\''
        print(email)
        print(cursor.execute("SELECT * FROM member;").fetchone())
        #print(cursor.execute("SELECT name FROM member where email = (%s);", [email]))
        return cursor.execute("SELECT name FROM member where email = (%s);", [email])

# def testQuery(): 
#     cursor.execute("SELECT * FROM instructor;")
#     return (cursor.fetchone()[1])

