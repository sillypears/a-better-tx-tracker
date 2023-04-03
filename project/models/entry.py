
from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, Date, Sequence, Float
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from dataclasses import dataclass

from .maker import Maker
from .sale import Sale
from .style import Style
from .tag import Tag
from .vendor import Vendor

from ..extentions import db

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
    image: str
    received: bool
    epoch: int
    purchase_date: str 
    received_date: str
    sold_date: str
    is_sold: bool
    will_sell: bool
    notes: str
    count_include: int
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
    image = Column(String(500))
    received = Column(Boolean, server_default=expression.true(), nullable=False)
    epoch = Column(Integer, nullable=False)
    purchase_date = Column(Date, nullable=False)
    received_date = Column(Date, nullable=False)
    sold_date = Column(Date, nullable=False)
    notes = Column(String(500))
    is_sold = Column(Boolean, server_default=expression.false(), nullable=False)
    will_sell = Column(Boolean, server_default=expression.true(), nullable=False)
    count_include = Column(Boolean, server_default=expression.true(), nullable=False)
    sculpt_style_id = Column(Integer, ForeignKey('styles.id'), nullable=False, default=1)
    
    maker_name = relationship("Maker", primaryjoin=("and_(Entry.maker_id==Maker.id)"), backref="makers")
    vendor_name = relationship("Vendor", primaryjoin=("and_(Entry.vendor_id==Vendor.id)"), backref="vendors")
    sale_name = relationship("Sale", primaryjoin=("and_(Entry.sale_id==Sale.id)"), backref="sales")
    tags = relationship("Tag", primaryjoin=("and_(Entry.id==Tag.entry_id)"), backref="tags")
    sculpt_style = relationship("Style", primaryjoin=("and_(Entry.sculpt_style_id==Style.id)"), backref="styles")

    # def to_dict(self):
    #     return dict(id=self.id, user_id=self.user_id, maker_id=self.maker_id, maker_name=self.maker_name.name, maker_display=self.maker_name.display, epoch=self.epoch, raffle_link=self.raffle_link, notes=self.notes, result=self.result, date=self.date)
    
    def __str__(self):
        return f"{self.id} > {self.display_name}/{self.colorway} -> {self.clw_num}/{self.clw_total}: {self.received}"