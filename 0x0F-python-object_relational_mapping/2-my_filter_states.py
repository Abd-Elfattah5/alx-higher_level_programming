#!/usr/bin/python3


"""this is a module to execute simple queries and test MySQLdb module"""


import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database_name)
    cur = db.cursor()
    qry = """SELECT * FROM states \
             WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC
          """.format(sys.argv[4])

    cur.execute(qry)
    for e in cur.fetchall():
        print(e)
    cur.close()
    db.close()
