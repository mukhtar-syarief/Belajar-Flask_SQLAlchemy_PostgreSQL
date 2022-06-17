import hashlib
import psycopg2
conn = psycopg2.connect(
   database="artikeldb", user='postgres', password='m03kht4r1999', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
conn.autocommit = True

sql_insert_users = """INSERT INTO users (nama, email, password) VALUES (%s, %s, %s)"""
sql_select_users = """SELECT * FROM users WHERE email = %s AND password = %s """

def create(nama, email, password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    insert = (nama, email, password)
    cur.execute (sql_insert_users, insert)
    return "Data Berhasil"

    
def account_login(email,password):
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    insert = (email,password)
    cur.execute(sql_select_users, insert)
    user = cur.fetchone()
    if user == None:
        return False
    else:
        user = {'id':user[0],
            'nama': user[1],
            'email': user[2]}
        return user

# account_login("m.angelica74@mail.com", "12345678")