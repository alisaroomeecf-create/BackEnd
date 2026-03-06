import os
from datetime import datetime

import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/alchemy_backend"
engine = create_async_engine(DATABASE_URL, echo=False)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase): pass


class Categories(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    products = relationship("Products", back_populates="category")


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'))

    category = relationship("Categories", back_populates="products")
    order_items = relationship("OrderItems", back_populates="product")


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)

    orders = relationship("Orders", back_populates="customer")


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    order_at = Column(DateTime, default=datetime.now(), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItems", back_populates="order")


class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    order = relationship("Orders", back_populates="order_items")
    product = relationship("Products", back_populates="order_items")
