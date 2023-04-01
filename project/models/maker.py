
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

from ..extentions import db

@dataclass
class Maker(db.Model):
    id: int
    name: str
    ka_id: str
    ka_name: str
    display: str
    instagram:str 
    
    __tablename__ = "makers"
    TABLE_NAME = Sequence('makers_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(100), nullable=False)
    ka_id= Column(String(12), nullable=False)
    ka_name = Column(String(100), nullable=False)
    display = Column(String(100), nullable=False)
    instagram = Column(String(100))
    
    def __str__(self):
        return f"{self.display} found at {self.instagram}"

