from dbcm_base import UseDatabase

dbconfig = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "vsearch",
    "database": "vsearchlogdb"
}

with UseDatabase(dbconfig) as cursor:
    sql = """show tables"""
    cursor.execute(sql)
    data = cursor.fetchall()

print(data)
