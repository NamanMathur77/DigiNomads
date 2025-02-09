from pydantic import BaseModel
from coordinate import Coordinate
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Base class for models
Base = declarative_base()

# Define the User model
class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    city_ascii = Column(String)
    country = Column(String)
    population = Column(Integer)
    lat = Column(Integer)
    lng = Column(Integer)