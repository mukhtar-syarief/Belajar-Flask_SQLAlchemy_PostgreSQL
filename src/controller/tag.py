from src.models.tags import Tags
from src.models.models import s


def all_tags():
    all_tag = s.query(Tags).all()