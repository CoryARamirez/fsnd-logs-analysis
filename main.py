#!/usr/bin/env python3

import psycopg2
from sql import query


def main(connection):
    print("""Setting up Udacity Log Analysis Program\n
    RE: FSND - Project 1 - Cory A. Ramirez""")

    ###########################################################################
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
        print("Rank {rank}: \"{name}\" with {views} views.".format(
            rank=i+1, name=record[0], views=record[1]))

    ###########################################################################

    # Which authors got the most page views?
    try:
        results = query("""SELECT authors.name, count (*)
            AS results from log, authors, articles
            WHERE log.status = '200 OK'
            AND articles.slug = substr(log.path, 10)
            AND authors.id = articles.author
            GROUP BY authors.name
            ORDER BY results desc""", connection)

    except Exception as e:
        print("Query error:", e)

    print("Authors with the most page views: ")

    for i, record in enumerate(results):
        print("Rank {rank}: \"{name}\" with {views} views.".format(
            rank=i+1, name=record[0], views=record[1]))

    ###########################################################################

    # Which days had greater than 1% of HTTP errors?
    try:
        results = query("""SELECT errors.date, errors.err/errors.total * 100
        AS percentage
        FROM (SELECT cast(time AS date) as date,
        COUNT(*) AS total,
        CAST(sum(cast(status  != '200 OK' as int)) AS float) AS err
        FROM log
        GROUP BY date) AS errors
        WHERE errors.err/errors.total > 0.01;""", connection)

    except Exception as e:
        print("Query error:", e)

    print("Days with HTTP errors larger than 1% of all errors: ")

    print(
        "Date: "
        + str(results[0][0])
        + " with number of errors totaling "
        + "{0:0.1f}".format(results[0][1])
        + "%."
    )

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
