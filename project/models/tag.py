
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

from ..extentions import db
    
@dataclass
class Tag(db.Model):
    id: int
    name: str
    entry_id: int
    
    __tablename__ = "tags"
    TABLE_NAME = Sequence('tags_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(20), nullable=False)
    entry_id = Column(Integer, ForeignKey('entries.id'), nullable=False)
    
    def __str__(self):
        return f""
