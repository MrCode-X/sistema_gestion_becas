import MySQLdb
conn = MySQLdb.connect(host='localhost', user='admin', passwd='123456', db='becas_db')
cur = conn.cursor()
cur.execute('SHOW TABLES')
print('TABLES:')
for row in cur.fetchall():
    print(row[0])
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='becas_db'")
print('\nINFORMATION_SCHEMA:')
for row in cur.fetchall():
    print(row[0])
conn.close()
