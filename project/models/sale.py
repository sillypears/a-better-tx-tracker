
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

from ..extentions import db

@dataclass    
class Sale(db.Model):
    __tablename__ = "sales"
    id: int
    name: str
    display: str
    
    TABLE_NAME = Sequence('sales_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(20), nullable=False)
    display = Column(String(20), nullable=False)
    
    def __str__(self):
        return f""

