
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

db = SQLAlchemy()

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

@dataclass    
class Style(db.Model):
    __tablename__ = "styles"
    id: int
    name: str
    display: str
    
    TABLE_NAME = Sequence('styles_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(20), nullable=False)
    display = Column(String(20), nullable=False)
    
    def __str__(self):
        return f""
    
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

@dataclass    
class Entry(db.Model):
    id: int
    maker_id: int
    vendor_id: int
    colorway: str
    sculpt_name: str
    display_name: str
    clw_num: int
    clw_total: int
    price: float
    adjustment: float
    retail: float
    sale_id: int
    sale_post: str
    result: int
    epoch: int
    purchase_date: str 
    received_date: str
    sold_date: str
    sculpt_style_id: int
    maker_name: Mapped[str]
    vendor_name: Mapped[str]
    sale_name: Mapped[str]
    tags: Mapped[str]
    sculpt_style: Mapped[str]

    __tablename__ = "entries"
    TABLE_NAME = Sequence('entries_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    maker_id = Column(Integer, ForeignKey('makers.id'), nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.id'), nullable=False)
    colorway = Column(String(100), nullable=False)
    sculpt_name = Column(String(100), nullable=False)
    display_name = Column(String(100), nullable=False)
    clw_num = Column(Integer, nullable=False)
    clw_total = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    adjustment = Column(Float, nullable=False)
    retail = Column(Float, nullable=False)
    sale_id = Column(Integer, ForeignKey('sales.id'), nullable=False)
    sale_post = Column(String(500))
    result = Column(Boolean, server_default=expression.true(), nullable=False)
    epoch = Column(Integer, nullable=False)
    purchase_date = Column(Date, nullable=False)
    received_date = Column(Date, nullable=False)
    sold_date = Column(Date, nullable=False)
    sculpt_style_id = Column(Integer, ForeignKey('styles.id'), nullable=False, default=1)
    maker_name = relationship("Maker", primaryjoin=("and_(Entry.maker_id==Maker.id)"), backref="makers")
    vendor_name = relationship("Vendor", primaryjoin=("and_(Entry.vendor_id==Vendor.id)"), backref="vendors")
    sale_name = relationship("Sale", primaryjoin=("and_(Entry.sale_id==Sale.id)"), backref="sales")
    tags = relationship("Tag", primaryjoin=("and_(Entry.id==Tag.entry_id)"), backref="tags")
    sculpt_style = relationship("Style", primaryjoin=("and_(Entry.sculpt_style_id==Style.id)"), backref="styles")

    # def to_dict(self):
    #     return dict(id=self.id, user_id=self.user_id, maker_id=self.maker_id, maker_name=self.maker_name.name, maker_display=self.maker_name.display, epoch=self.epoch, raffle_link=self.raffle_link, notes=self.notes, result=self.result, date=self.date)
    
    def __str__(self):
        return f"{self.display_name}/{self.colorway} -> {self.clw_num}/{self.clw_total}"