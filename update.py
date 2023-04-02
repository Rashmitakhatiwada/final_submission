from establish_connection import establish_connection

def update(id, to_change, value):
    cursor = establish_connection()

    sql = f"""
    UPDATE FINAL_STUDENTS 
    SET {to_change.upper()}='{value}' 
    WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been updated. Do you want to continue? (y/n)")
    return cont.lower() == 'y'