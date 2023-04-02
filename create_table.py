from  establish_connection import establish_connection

cursor = establish_connection()

cursor.execute("drop table if exists myshare")
sql="""
create table final_students(
id char(5),
name char(100),
departments char(100)
)
"""
cursor.execute(sql)
print("table created succesfully !!")
