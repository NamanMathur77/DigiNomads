from fastapi import Depends
from typing import List
import config
from coordinate import Coordinate
from city import City

localSession = config.Config
app = config.create_app()

@app.get("/cities")
def get_cities(db: localSession.SessionLocal = Depends(localSession.get_db)):
    cities_list : List[City]
    cities_list = db.query(City).limit(10).all()
    for city in cities_list:
        city.coordinates = Coordinate(city.lat, city.lng)
    return cities_list
