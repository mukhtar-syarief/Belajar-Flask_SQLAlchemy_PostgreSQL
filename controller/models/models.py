from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship
from flask_login import UserMixin

Base = declarative_base()


class Users(Base,UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    nama = Column(Text)
    email = Column(Text, unique=True)
    password = Column(Text)
    created_at = Column(DateTime, default=func.now())
    artikel = relationship(
        "Artikels",
        back_populates="user",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
    )
    komentar = relationship(
        "Comments",
        back_populates="user",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
    )

    def __repr__(self):
        return f"Users(id={self.id}, nama={self.nama}, email={self.email}, password={self.password})"


class Artikels(Base):
    __tablename__ = 'artikels'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"))    
    judul = Column(Text)
    konten = Column(Text)
    created_at = Column(DateTime, default=func.now())
    modified = Column(DateTime, default=func.now(), onupdate=func.now())
    user = relationship("Users", back_populates="artikel")
    komentar = relationship(
        "Comments",
        back_populates="artikel",
        cascade="all, delete, delete-orphan",
        passive_deletes=True,
    )
    def __repr__(self):
        return f"Artikels(id={self.id}, user_id = {self.user_id}, judul = {self.judul}, konten = {self.konten})"


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key = True)
    nama = Column(Text)

    def __repr__(self):
        return f"Tags(id = {self.id}, nama = {self.nama})"


class Artikel_tag(Base):
    __tablename__ = 'artikel_tag'
    id = Column(Integer, primary_key = True)
    artikel_id = Column(Integer, ForeignKey("artikels.id", ondelete="CASCADE"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    def __repr__(self):
        return f"Artikel_tag(id = {self.id}, artikel_id = {self.artikel_id}, tag_id = {self.tag_id})"


class Comments(Base):
    __tablename__ = 'coments'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    artikel_id = Column(Integer, ForeignKey("artikels.id", ondelete="CASCADE"))
    komentar = Column(Text)
    created_at = Column(DateTime, default=func.now())
    artikel = relationship("Artikels", back_populates="komentar")
    user = relationship("Users", back_populates="komentar")
    

    def __repr__(self):
        return f"Comments(id = {self.id}, user_id = {self.user_id}, artikel_id = {self.artikel_id}, komentar = {self.komentar})"


class Categories(Base):
    __tablename__ = "kategori"
    id = Column(Integer, primary_key = True)
    kategori = Column(Text)

    def __repr__(self):
        return f"Categories(id = {self.id}, kategori = {self.kategori}"
    

class Artikel_Categories(Base):
    __tablename__ = "artikel_categories"
    id = Column(Integer, primary_key = True)
    artikel_id = Column(Integer, ForeignKey("artikels.id", ondelete="CASCADE"))
    categories_id = Column(Integer, ForeignKey("kategori.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"Artikel_Categories(id = {self.id}, artikel_id = {self.artikel_id}, categories = {self.categories_id}"