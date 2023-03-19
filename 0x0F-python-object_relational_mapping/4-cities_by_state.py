#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("\
    SELECT c.id, c.name, s.name FROM cities AS c\
    JOIN states AS s\
    ON s.id = c.state_id\
    ORDER BY c.id ASC\
    ")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
