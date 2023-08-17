#!/usr/bin/python3
""" Select States That begins with 'N' Module

This Module define a python script that queries a database
to print all cities with there corresponding states
"""

import MySQLdb as sql
import sys

if __name__ == "__main__":  # runs only as a script
    _, username, password, dbname, state_name = sys.argv
    db = sql.connect(
        host="localhost", port=3306,
        user="{}".format(username),
        passwd="{}".format(password),
        db="{}".format(dbname)
        )
    cursor = db.cursor()
    command = (
            '''WITH mytable1 AS (SELECT c.name
            FROM cities c JOIN states s
            ON c.state_id = s.id WHERE s.name LIKE "{}"
            ORDER BY c.id ASC)
            SELECT DISTINCT name FROM mytable1
            '''
            )
    cursor.execute(command.format(state_name))
    states = [item[0] for item in cursor.fetchall()]
    print(', '.join(states))
