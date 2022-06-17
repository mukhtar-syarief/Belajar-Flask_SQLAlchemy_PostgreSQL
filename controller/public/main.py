import psycopg2
conn = psycopg2.connect(
   database="artikeldb", user='postgres', password='m03kht4r1999', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
conn.autocommit = True

sql_select_user = """SELECT * FROM users WHERE email = %s """
sql_select_user_id = """SELECT * FROM users WHERE id = %s """

def find_user(email):
    email = (email,)
    cur.execute(sql_select_user, email)
    user = cur.fetchone()
    return user

def find_user_id(id):
    id = (id,)
    cur.execute(sql_select_user_id, id)
    user = cur.fetchone()
    return user

