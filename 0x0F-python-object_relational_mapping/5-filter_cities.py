#!/usr/bin/python3


"""this is a module to execute simple queries and test MySQLdb module"""


import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4].split('\'')[0]

    db = MySQLdb.connect(user=username, passwd=password, db=database_name)
    cur = db.cursor()
    qry = """SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = '{}'
             ORDER BY cities.id ASC
          """.format(state_name)

    cur.execute(qry)
    data = [e[0] for e in cur.fetchall()]
    print(*data, sep=',')
    cur.close()
    db.close()
