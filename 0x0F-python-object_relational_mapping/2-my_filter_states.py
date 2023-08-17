#!/usr/bin/python3
""" Select States That begins with 'N' Module

This Module define a python script that queries a database
to print all states with names that matches a search argument
"""

import MySQLdb as sql
import sys

if __name__ == "__main__":  # runs only as a script
    _, username, password, dbname, search = sys.argv
    db = sql.connect(
        host="localhost", port=3306,
        user="{}".format(username),
        passwd="{}".format(password),
        db="{}".format(dbname)
        )
    cursor = db.cursor()
    command = '''SELECT * FROM states WHERE name LIKE "{}"'''
    cursor.execute(command.format(search))
    for item in cursor.fetchall():
        print(item)
