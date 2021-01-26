import mysql.connector

dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "vsearch",
    "database": "vsearchlogdb"
}

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

sql = """
insert into log (phrase, letters, ip, browser_string, results)
values (%s, %s, %s, %s, %s)
"""

cursor.execute(sql, ("galaxy", "xyz", "127.0.0.1", "Firefox", "set()"))
conn.commit()

sql = """select * from log"""
cursor.execute(sql)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
