from establish_connection import establish_connection

def delete(id):
    id = input("enter the id of a student you want to delete")
    cursor = establish_connection()
    sql = f"""
    DELETE FROM final_STUDENTS WHERE ID='{id}'
    """

    cursor.execute(sql)
    print("data deleted successfully !!")
    cont = input("The student has been deleted. Do you want to continue? (y/n)")
    return cont.lower() == 'y'