from src.controller import user
from unittest import mock

def test_login_user_benar():
    data_user = user.user_login("babulilmi@gmail.com", "123456789")
    user_benar(data_user)

def test_login_email_huruf_besar():
    data_user = user.user_login("baBulilmI@gmaiL.Com", "123456789")
    user_benar(data_user)


def user_benar(data_user):
    assert data_user.email == "babulilmi@gmail.com"
    assert data_user.password == "25f9e794323b453885f5181f1b624d0b"

# def test_daftar_user_baru():
#     data_user = user.create_user("Mulyadi Rahmat", "rahmatmulyadi@gmail.com", "123456789")
#     assert data_user.nama == "Mulyadi Rahmat"
#     assert data_user.email == "rahmatmulyadi@gmail.com"
#     assert data_user.password == "25f9e794323b453885f5181f1b624d0b"




#####################################
######-----AKHIRNYA PASSED-----######
#####################################

