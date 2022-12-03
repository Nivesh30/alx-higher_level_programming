#!/usr/bin/python3
'''
Lists all states from a database containing states data
USAGE:
    ./0-select_states.py <USER_NAME> mysql <PASSWORD> <DATABASE_NAME>
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
            db=sys.argv[3],
            user=sys.argv[1],
            password=sys.argv[2])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    [print(state) for state in cursor.fetchall()]
