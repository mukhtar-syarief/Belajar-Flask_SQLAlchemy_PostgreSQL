from src.controller.user import user_login
from unittest import mock

def user():
    return NotImplementedError("Nilai test belum dimasukkan")



def user_benar(user):
    assert user.email == "babulilmi@gmail.com"
    assert user.password == "12345789"