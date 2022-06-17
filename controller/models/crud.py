from sqlalchemy import and_, create_engine
from config import DATABASE_URL
from models import Base, Comments, Users, Artikels
from sqlalchemy.orm import sessionmaker
import hashlib


engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
s = Session()

Base.metadata.create_all(engine)

# Base.metadata.drop_all(engine)


#mencari semua user
def users():
    users = s.query(Users).all()
    list_user=[]
    for user in users:
        user = {'id': user.id,
        'nama': user.nama}
        list_user.append(user)
    return list_user

#membuat login
def user_login(email,password):
    password = hashlib.md5(password.encode())
    hashed_password = password.hexdigest()
    user = s.query(Users).filter(and_(Users.email == email, Users.password == hashed_password)).first()
    if user == None:
        return False
    else:
        return user

#mencari user dari email
def find_user_by_email(email):
    user = s.query(Users).filter(Users.email == email).first()
    return user

#mencari user dari id
def find_user_by_id(id):
    user = s.query(Users).filter(Users.id == id).first()
    return user


#membuat user baru / daftar user baru
def create_user(nama, email, password):
    password = hashlib.md5(password.encode())
    hashed_password = password.hexdigest()
    user = Users(nama= f"{nama}", email = f"{email}", password= f"{hashed_password}")
    s.add(user)
    s.commit()


#mencari semua artikel
def all_artikels():
    artikels = s.query(Artikels).all()
    list_artikel=[]
    for artikel in artikels:
        nama_user = find_user_by_id(artikel.user_id).nama
        artikel = {'id': artikel.id,
        'user_id': artikel.user_id,
        'nama_user': nama_user,
        'judul': artikel.judul,
        'konten': artikel.konten}
        list_artikel.append(artikel)
    return list_artikel

#mencari artikel dari id
def find_artikel_by_id(id):
    artikel = s.query(Artikels).filter(Artikels.id == id).first()
    return artikel

#mengedit artikel
def update_artikel(id, judul, konten):
    artikel = find_artikel_by_id(id)
    artikel.judul = judul
    artikel.konten = konten

#menghapus artikel
def deleting_artikel(id):
    artikel = s.query(Artikels).filter(Artikels.id == id)
    artikel.delete()
    s.commit()

#membuat artikel
def created_post(user_id, judul, konten):
    post = Artikels(user_id= f"{user_id}", judul = f"{judul}", konten= f"{konten}")
    s.add(post)
    s.commit()

#membuat komentar
def created_komentar(user_id, artikel_id, komentar):
    komentar = Comments(user_id = f"{user_id}", artikel_id = f"{artikel_id}", komentar = komentar)
    s.add(komentar)
    s.commit()

#mencari komentar dengan id artikel
def find_komentar(artikel_id):
    comments = s.query(Comments).filter(Comments.artikel_id == artikel_id).all()
    komentar = []
    for comment in comments:
      user = find_user_by_id(comment.user_id)
      comment = {'nama': user.nama,
      'komentar': comment.komentar}
      komentar.append(comment)
    return komentar