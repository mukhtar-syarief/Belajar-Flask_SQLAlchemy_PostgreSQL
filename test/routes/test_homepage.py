import pytest
from server import app

@pytest.fixture
def client():
    return app.test_client()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_sign_up_page(client):
    response = client.get("/signup")
    assert response.status_code == 200

def test_article_page(client):
    response = client.get("/article")
    assert response.status_code == 302

def test_new_article_page(client):
    response = client.get("/new")
    assert response.status_code == 302

def test_new_article_page_post(client):
    response = client.post("/new")
    assert response.status_code == 302

def test_article_detail_page(client):
    response = client.get("/article/1")
    assert response.status_code == 302

def test_article_edit_page(client):
    response = client.get("/article/1/edit")
    assert response.status_code == 302

def test_article_edit_page_post(client):
    response = client.post("/article/1/edit")
    assert response.status_code == 302

def test_comments_page(client):
    response = client.get("/article/1/comments")
    assert response.status_code == 302

def test_comments_page_post(client):
    response = client.post("/article/1/comments")
    assert response.status_code == 302

def test_user_page(client):
    response = client.get("/Salman Fahriza")
    assert response.status_code == 302

def test_logout_page(client):
    response = client.get("/logout")
    assert response.status_code == 302