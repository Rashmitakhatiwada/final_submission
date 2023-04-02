from establish_connection import establish_connection

def read(id):
    id = input("Enter the student ID ")
    cursor = establish_connection()
    sql = f"""
    select * from final_students
    where id='{id}'
    """

    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cont = input("a new student is added do you wish to continue(Y/N)")
    return cont.lower() == 'y'