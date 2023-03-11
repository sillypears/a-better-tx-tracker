
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Maker(db.Model):
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

class Vendor(Model):
    __tablename__ = "vendors"
    TABLE_NAME = Sequence('vendors_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(100), nullable=False)
    display = Column(String(100), nullable=False)
    website = Column(String(100))

    def __str__(self):
        return f""
    
class Sale(Model):
    __table_name__ = "sales"
    TABLE_NAME = Sequence('sales_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(20), nullable=False)
    display = Column(String(20), nullable=False)
    
    def __str__(self):
        return f""
    
class Tag(Model):
    __table_name__ = "tags"
    TABLE_NAME = Sequence('tags_id_seq', start=1)
    id = Column(Integer, TABLE_NAME, unique=True, primary_key=True, server_default=TABLE_NAME.next_value())
    name = Column(String(20), nullable=False)
    entry_id = Column(Integer, ForeignKey('entry.id'), nullable=False)
    
    def __str__(self):
        return f""
    
class Entry(Model):
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
    sale_id = Column(Integer, ForeignKey('sale.id'), nullable=False)
    sale_post = Column(String(500))
    result = Column(Boolean, server_default=expression.true(), nullable=False)
    epoch = Column(Integer, nullable=False)
    purchase_date = Column(Date, nullable=False)
    received_date = Column(Date, nullable=False)
    sold_date = Column(Date, nullable=False)
    
    maker_name = relationship("Maker", primaryjoin=("and_(Entry.maker_id==Maker.id)"), backref="makers")
    vendor_name = relationship("Vendor", primaryjoin=("and_(Entry.vendor_id==Vendor.id)"), backref="vendors")
    sale_name = relationship("Sale", primaryjoin=("and_(Entry.sale_id==Sale.id)"), backref="sales")
    # tags = relationship("Tags", primaryjoin=("and_(Entry.id==Tag.entry_id)"), backref="tags")

    # def to_dict(self):
    #     return dict(id=self.id, user_id=self.user_id, maker_id=self.maker_id, maker_name=self.maker_name.name, maker_display=self.maker_name.display, epoch=self.epoch, raffle_link=self.raffle_link, notes=self.notes, result=self.result, date=self.date)

    
    def __str__(self):
        return f""