import psycopg2


conn = psycopg2.connect(
    database='online_store',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5432
)
cursor_obj = conn.cursor()
cursor_obj.execute('SELECT * FROM auth_user')
result = cursor_obj.fetchall()
print("Result: ", "\n", result)