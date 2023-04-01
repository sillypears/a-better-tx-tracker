
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

from ..extentions import db

@dataclass
class Vendor(db.Model):
    id: int
    name: str
    display: str
    website: str
    
    __tablename__ = "vendors"
    TABLE_NAME = Sequence('vendors_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(100), nullable=False)
    display = Column(String(100), nullable=False)
    website = Column(String(100))

    def __str__(self):
        return f""
