from fastapi import Depends, Query
from sqlalchemy.orm import Session
from typing import List
import config
from coordinate import Coordinate
from city import City

app = config.create_app()

@app.get("/cities")
def get_cities(
    db: Session = Depends(config.Config.get_db),
    limit: int = Query(10, description="Number of cities to fetch"),
    offset: int = Query(0, description="Number of cities to skip")):
    cities_list : List[City]
    cities_list = db.query(City).offset(offset).limit(limit).all()
    for city in cities_list:
        city.coordinates = Coordinate(city.lat, city.lng)
    return cities_list
