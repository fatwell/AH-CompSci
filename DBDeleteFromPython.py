#fatwell
import mysql.connector

con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sloco')
c = con.cursor()
c.execute("""DELETE FROM client WHERE Client_ID = 3""")
con.commit()
c.close 