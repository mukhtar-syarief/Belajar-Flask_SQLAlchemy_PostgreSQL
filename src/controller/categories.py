from src.models.categories import Categories
from src.models.models import s

def all_categories():
    list_categorie = s.query(Categories).order_by(Categories.id)
    return list_categorie

def find_categorie_by_id(id):
    categorie = s.query(Categories).filter(Categories.id == id)
    return categorie

def find_categorie_by_name(categorie):
    categories = s.query(Categories).filter(Categories.categories == categorie).first()
    return categories