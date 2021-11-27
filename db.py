import psycopg2

def testQuery(): 
    db = psycopg2.connect(host='localhost', 
    dbname='practice', user='postgres', password='0130', port='5432')
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM instructor;")
    return (cursor.fetchone()[1])

