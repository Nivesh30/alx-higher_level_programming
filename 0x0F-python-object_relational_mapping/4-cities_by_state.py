#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         port=3306,
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT C.id, C.name, S.name \
            FROM states S, cities C \
            WHERE S.id  = C.state_id \
            ORDER BY C.id ASC")
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
