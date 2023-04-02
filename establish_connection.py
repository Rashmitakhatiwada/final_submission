import psycopg2


def establish_connection():
    conn = psycopg2.connect(
        database="student",
        user="peshal",
        password="password",
        host="127.0.0.1",
        port=5432
    )

    conn.autocommit = True
    print("connection established successfully !!")
    cursor = conn.cursor()
    return cursor