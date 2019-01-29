import pymssql

conn = pymssql.connect(host='host',user='user',password ='password', database='database')
cur = conn.cursor()
cur.execute('select top 100 * from enforce')
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
