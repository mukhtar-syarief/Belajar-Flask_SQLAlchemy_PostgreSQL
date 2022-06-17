from controller.public.main import find_user_id
import psycopg2
conn = psycopg2.connect(
   database="artikeldb", user='postgres', password='m03kht4r1999', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
conn.autocommit = True

sql_select_user = """SELECT * FROM users WHERE nama = %s"""
sql_select_user_id = """SELECT * FROM users WHERE id = %s"""


sql_select_artikels = """SELECT * FROM artikels"""
sql_selecst_artikels_id = """SELECT * FROM artikels WHERE id = %s """
sql_insert_artikels = """INSERT INTO artikels (user_id, judul, konten) VALUES (%s, %s, %s)"""
sql_delete_artikel = """DELETE FROM artikels WHERE id = %s"""
sql_update_artikel = """UPDATE artikels SET judul = %s, konten = %s WHERE id = %s"""


sql_insert_coments = "INSERT INTO coments (user_id, artikel_id, komentar) VALUES (%s, %s, %s )"
sql_select_coments = "SELECT * FROM coments WHERE artikel_id = %s"

def create_post(nama, judul, kontent):
   nama = (nama,)
   cur.execute(sql_select_user, nama)
   user_id = cur.fetchone()[0]
   insert = (user_id,judul,kontent)
   cur.execute(sql_insert_artikels, insert)
   return "Data Berhasil Dibuat..!!"

def list_post():
   cur.execute(sql_select_artikels)
   user_artikels = cur.fetchall()
   return user_artikels

def user_artikel(user_id):
   insert = (user_id,)
   cur.execute(sql_select_user_id, insert)
   user_artikel = cur.fetchone()
   user_artikel = {
      'id': user_artikel[0],
      'nama': user_artikel[1],
      'email': user_artikel[2]
   }
   return user_artikel

def delete_artikel(id):
   id = int(id)
   id = (id,)
   cur.execute(sql_delete_artikel, id)
   return 0

def find_artikel(id):
   id = (id,)
   cur.execute(sql_selecst_artikels_id, id)
   artikel = cur.fetchone()
   return artikel

def update_artikel(id, judul, konten):
   insert = (judul, konten, id)
   cur.execute(sql_update_artikel, (insert))
   return "Data Berhasil diupdate"

def create_coment(user_id, artikel_id, komentar):
   insert = (user_id, artikel_id, komentar)
   cur.execute(sql_insert_coments, insert)
   return "Komentar telah dibuat..!!"

def find_comment(artikel_id):
   insert = (artikel_id,)
   cur.execute(sql_select_coments, insert)
   comments = cur.fetchall()
   komentar = []
   for comment in comments:
      user = find_user_id(comment[1])
      comment = {'nama': user[1],
      'komentar': comment[3]}
      komentar.append(comment)
   return komentar
   
