#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """
if __name__ == '__main__':

    import mysqldb
    import sys

    db = mysqldb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    cur = db.curcor()
    cur.execute("SELECT * FROM states
                where name LIKE 'N%'
                ORDER BY states.id ASC")

    states = cur.fetchall()
    for state in states:
        print(state)