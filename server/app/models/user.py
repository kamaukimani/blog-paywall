from app.db import db 
from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy_serializer import SerializerMixin 
from typing import List

class User(db.Model,SerializerMixin):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

    articles:Mapped[List["Article"]]=relationship(back_populates="user",cascade="all,delete-orphan")


    def __repr__(self):
        return f"<User {self.id} Name:{self.name}>"