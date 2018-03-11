import pymysql

db = pymysql.connect(host="192.168.10.110", user="root", passwd="Admin", db="mysql")

cur = db.cursor()

cur.execute("SELECT url FROM articles")

row = cur.fetchall()

print(row[9551])