from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings

DeclarativeBase = declarative_base()

def db_connect():
  return create_engine(URL(**settings.DATABASE))

def create_deals_table(engine):
  DeclarativeBase.metadata.create_all(engine)

class Deals(DeclarativeBase):
  __tablename__ = "deals"

  id             = Column(Integer, primary_key=True)
  title          = Column("title", String)
  description    = Column("description", String, nullable=True)
  link           = Column("link", String, nullable=True)
  location       = Column("location", String, nullable=True)
  category       = Column("category", String, nullable=True)
  original_price = Column("original_price", String, nullable=True)
  price          = Column("price", String, nullable=True)

