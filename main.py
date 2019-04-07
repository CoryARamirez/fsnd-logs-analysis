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
    

def main(connection):
    print("Setting up Udacity Log Analysis Program\nRE: FSND - Project 1 - Cory A. Ramirez")
    
    # What articles have been accessed the most of all time?
    try:
        results = query("""SELECT articles.title, COUNT(*)
            AS results from articles, log
            WHERE log.status = '200 OK'
            AND articles.slug = substr(log.path, 10)
            GROUP BY articles.title
            ORDER BY results desc
            limit 3;""", connection)
            
    except Exception as e:
        print("Query error:", e)
    
    print("Top three most accessed articles: ")
    
    for i, record in enumerate(results):
        print("Rank " + str(i + 1) + ": " + record[0] + " with " + str(record[1]) + " views.")
    
    # Which authors got the most page views?
    try:
        results = query("""SELECT * from articles""", connection)
        
    except Exception as e:
        print("Query error:", e)
        
    print("Authors with the most page views: ")
    
    for i, record in enumerate(results):
        print(record)

    # Which days had greater than 1% of HTTP errors?
    
    # Close db connection
    db_conn.close()


if __name__ == "__main__":
    # Establsh connection to the database server.  Exit if unable to connect
    try:
        db_conn = psycopg2.connect("dbname=news")
        # Pass the established connection so the application can re-use it
        main(db_conn)
        
    except Exception as e:
        print("Database error: ", e)
        exit()