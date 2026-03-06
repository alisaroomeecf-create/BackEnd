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


class Registrations (Base):
    __tablename__ = 'registration'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    contact = Column(String)
    mail = Column(String)
    password = Column(String)

class Flights (Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, index=True)


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    order_at = Column(DateTime, default=datetime.now(), nullable=False)

class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
