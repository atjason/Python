
import sqlite3

try:
  conn = sqlite3.connect("tmp.db")

  cursor = conn.cursor()

  try:
    cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")

    cursor.execute("insert into user (id, name) values ('1', 'Tom')")

    print cursor.rowcount
  except Exception as e:
    print e
    
  cursor.execute("select * from user where id=?", ('1',))

  values = cursor.fetchall()
  print values

except Exception as e:
  print e

finally:
  cursor.close()

  conn.commit()
  conn.close()

