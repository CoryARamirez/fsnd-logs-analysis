import psycopg2

def query(statement, conn):
    try:
        # Instantiate a cursor that will be used to interact with the db
        db_cursor = conn.cursor()
        
    except Exception as e:
        print("Cursor error:", e)
        exit()
        
    # Execute query statement
    db_cursor.execute(statement)
    
    results = db_cursor.fetchall()
    
    db_cursor.close()
    
    return results
