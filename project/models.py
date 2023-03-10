from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String, Boolean, Date, Sequence
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship

# from . import db

db = SQLAlchemy()

class Maker(db.Model):
    __tablename__ = "makers"

    id = db.Column(db.Integer, Sequence('makers_id_seq'), unique=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ka_id= db.Column(db.String(12), nullable=False)
    ka_name = db.Column(db.String(100), nullable=False)
    display = db.Column(db.String(100), nullable=False)
    instagram = db.Column(db.String(100))

class Vendor(db.Model):
    __tablename__ = "vendors"

    id = db.Column(db.Integer, Sequence('makers_id_seq'), unique=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    display = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(100))

class Sale(db.Model):
    __table_name__ = "sales"
    
    id = db.Column(db.Integer, Sequence('sales_id_seq'), unique=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    display = db.Column(db.String(20), nullable=False)
    
class Tag(db.Model):
    __table_name__ = "tags"
    
    id = db.Column(db.Integer, Sequence('tags_id_seq'), unique=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'), nullable=False)
    
class Entry(db.Model):
    __tablename__ = "entries"

    id = db.Column(db.Integer, Sequence('entries_id_seq'), unique=True, primary_key=True)
    maker_id = db.Column(db.Integer, db.ForeignKey('maker.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    colorway = db.Column(db.String(100), nullable=False)
    sculpt_name = db.Column(db.String(100), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)
    clw_num = db.Column(db.Integer, nullable=False)
    clw_total = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    adjustment = db.Column(db.Float, nullable=False)
    retail = db.Column(db.Float, nullable=False)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    sale_post = db.Column(db.String(500))
    result = db.Column(db.Boolean, server_default=expression.true(), nullable=False)
    epoch = db.Column(db.Integer, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    received_date = db.Column(db.Date, nullable=False)
    sold_date = db.Column(db.Date, nullable=False)
    
    maker_name = db.relationship("Maker", primaryjoin=("and_(Entry.maker_id==Maker.id)"), backref="makers")
    vendor_name = db.relationship("Vendor", primaryjoin=("and_(Entry.vendor_id==Vendor.id)"), backref="vendors")
    sale_name = db.relationship("Sale", primaryjoin=("and_(Entry.sale_id==Sales.id)"), backref="sales")
    tags = db.relationship("Tags", primaryjoin=("and_(Entry.id==Tags.entry_id)"), backref="tags")

    # def to_dict(self):
    #     return dict(id=self.id, user_id=self.user_id, maker_id=self.maker_id, maker_name=self.maker_name.name, maker_display=self.maker_name.display, epoch=self.epoch, raffle_link=self.raffle_link, notes=self.notes, result=self.result, date=self.date)
