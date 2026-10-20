from app.db import db 
from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 

class User(db.Model,SerializerMixin):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

    articles:Mapped[list["Article"]]=relationship(back_populates="user",cascade="all,delete-orphan")