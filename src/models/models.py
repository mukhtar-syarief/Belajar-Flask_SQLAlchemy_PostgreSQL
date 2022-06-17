from src.models.articles import Articles
from src.models.artikel_tag_assosiation import ArticleTag
from src.models.users import Users
from src.models.tags import Tags
from src.models.comments import Comments
from src.models.config import db, DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind = engine)
s = Session()

db.metadata.create_all(engine)
