from establish_connection import establish_connection

def create():
    cursor = establish_connection()
    id = input("enter the id of a student")
    name = input("enter the name of a student")
    departments = input("enter the department of a student")

    # print(each)

    sql = f"""
    insert into final_students(ID,NAME,departments)
    VALUES('{id}','{name}','{departments}')
    """
    cont=input("a new student is added do you wish to continue(Y/N)")
    cursor.execute(sql)
    return cont.lower() == 'y'