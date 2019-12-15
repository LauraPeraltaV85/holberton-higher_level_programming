#!/usr/bin/python3
"""
Get all the states
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_dict = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3], charset="utf8")
    cur = db_dict.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
 LEFT JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_dict.close()
