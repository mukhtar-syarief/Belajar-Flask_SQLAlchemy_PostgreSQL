from src.models.users import Users
from src.models.models import s
from sqlalchemy import and_
import hashlib


#Membuat User Baru
def create_user(nama, email, password):
    password = hashlib.md5(password.encode())
    hash_password = password.hexdigest()
    user = Users(nama = f"{nama}", email = f"{email}", password = f"{hash_password}")
    s.add(user)
    s.commit()

#User Login
def user_login(email,password):
    email = email.lower()
    password = hashlib.md5(password.encode())
    hash_password = password.hexdigest()
    user = s.query(Users).filter(and_(Users.email == email, Users.password == hash_password)).first()
    if user == None:
        return False
    else:
        return user

#Mencari User Berdasarkan ID
def find_user_by_id(id):
    user = s.query(Users).filter(Users.id == id).first()
    return user

#Mencari User Berdasarkan Email
def find_user_by_email(email):
    user = s.query(Users).filter(Users.email == email).first()
    return user

def find_user_by_nama(nama_user):
    user = s.query(Users).filter(Users.nama == nama_user).first()
    return user