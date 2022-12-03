#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name  = %s \
            ORDER BY cities.id ASC", [sys.argv[4]])
    cities = cur.fetchall()
    length = len(cities)
    spc = ', '
    count = 0
    for city in cities:
        if count < length - 1:
            print(city[0]+spc, end='')
        else:
            print(city[0], end='')
        count += 1
    print()

    cur.close()
    db.close()
