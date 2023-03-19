#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import MySQLdb

if __name__ == '__main__':

     db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name
                 FROM states s, cities c
                 WHERE c.state_id = s.id
                 ORDER BY c.id ASC")
    cities = cur.fetchall()

    for citie in cities:
        print(citie)
