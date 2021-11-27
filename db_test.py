import psycopg2

db = psycopg2.connect(host='localhost', 
dbname='practice', user='postgres', password='0130', port='5432')
    
cursor = db.cursor()
cursor.execute("SELECT * FROM instructor;")
print(cursor.fetchone(), type(cursor.fetchone()))