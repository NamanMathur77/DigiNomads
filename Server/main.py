from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from city import City
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from coordinate import Coordinate

# MySQL database connection URL
DATABASE_URL = "mysql+pymysql://root:*october2020@localhost/nomad_database"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define the User model
class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    city_ascii = Column(String)
    country = Column(String)
    population = Column(Integer)
    lat = Column(Integer)
    lng = Column(Integer)


@app.get("/cities")
def get_cities(db: SessionLocal = Depends(get_db)):
    cities_list : List[City]
    cities_list = db.query(City).limit(10).all()
    for city in cities_list:
        city.coordinates = Coordinate(city.lat, city.lng)
    return cities_list
