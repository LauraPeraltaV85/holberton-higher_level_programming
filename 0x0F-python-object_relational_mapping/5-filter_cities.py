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
    cur.execute("SELECT cities.name FROM cities\
 JOIN states ON cities.state_id = states.id WHERE states.name\
 LIKE BINARY '{}' ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    cit = []
    for row in query_rows:
        cit.append(row[0])
    print(', '.join(cit))
    cur.close()
    db_dict.close()
