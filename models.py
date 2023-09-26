from database import Base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

product_order = Table ('product_order', # handles order-product relationship
                Base.metadata,
                Column('order_id', Integer, ForeignKey('orders.id')),
                Column('product_id', Integer, ForeignKey('products.id'))
                )

purchases = Table ('purchases', # handles user-product relationship
                   Base.metadata,
                   Column('user_id', Integer, ForeignKey('users.id')),
                   Column('product_id', Integer, ForeignKey('products.id'))
                   )

class User(Base):

    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    purchases = relationship('Product', secondary=purchases, backref='users')


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    orders = relationship('Order', secondary=product_order, backref='products')

class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    