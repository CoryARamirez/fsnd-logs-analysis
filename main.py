import psycopg2

def query(statement, cursor):
    # Execute query statement
    cursor.execute(statement)
    
    results = cursor.fetchall()
    
    return results
    

def main(db_conn):
    print("Setting up Udacity Log Analysis Program\nRE: FSND - Project 1 - Cory A. Ramirez")
    
    try:
        # Instantiate a cursor that will be used to interact with the db
        db_cursor = db_conn.cursor()
        
    except:
        print("Unable to instantiate database cursor.  Exiting")
        exit()
        
    # What articles have been accessed the most of all time?
    print("Top three most accessed articles:")
    
    results = query("""SELECT articles.id, COUNT(*)
        AS results from articles, logs
        WHERE log.status = '200 OK'
        AND articles.slug = substr(log.path, 20)
        GROUP BY articles.title
        ORDER BY results desc
        limit 3;
        """,
        db_cursor)
        
    print(results)
    
    # Which authors got the most page views?

    # Which days had greater than 1% of HTTP errors?
    
    # Close db connection
    db_conn.close()


if __name__ == "__main__":
    # Establsh connection to the database server.  Exit if unable to connect
    try:
        db_conn = psycopg2.connect("dbname=news")
        main(db_conn)
        
    except:
        print("Unable to connect to the news database..")
        exit()