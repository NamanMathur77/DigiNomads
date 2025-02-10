import json
from fastapi import Depends, Query
from models.DataModels.city import City
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import config
from coordinate import Coordinate
from models.ORM.city import CityORM

app = config.create_app()

@app.get("/cities")
def get_cities(
    db: Session = Depends(config.Config.get_db),
    limit: int = Query(10, description="Number of cities to fetch"),
    offset: int = Query(0, description="Number of cities to skip")):
    cities_list : List[CityORM]
    cities_list = db.query(CityORM).offset(offset).limit(limit).all()
    for city in cities_list:
        city.coordinates = Coordinate(city.lat, city.lng)
    return cities_list

@app.get("/closest-city")
def get_closest_cities(
    db: Session = Depends(config.Config.get_db),
    limit: int = Query(2, description="Number of closest cities to the given coordinate"),
    lat: float = Query(..., description="Latitude of the location"),
    lng: float = Query(..., description="longitude of the location")
):
    query= text("""
    SELECT id, city_ascii, lat, lng,
        (6371 * ACOS(COS(RADIANS(:lat)) * COS(RADIANS(lat)) * 
        COS(RADIANS(lng) - RADIANS(:lng)) + 
        SIN(RADIANS(:lat)) * SIN(RADIANS(lat)))) AS distance
        FROM cities
        ORDER BY distance ASC
        LIMIT :limit
    """)
    result = db.execute(query, {"lat": lat, "lng": lng, "limit": limit}).all()
    results = [tuple(row) for row in result]
    print(result)
    breakpoint
    if not result:
        return {"message": "No cities found"}

    return json.dumps(results)

@app.post("/cities")
def createCity(city: City, db: Session = Depends(config. Config.get_db)):
    new_city = CityORM(city_ascii = city.name, country = city.country, population = city.population, lat = city.lat, lng = city.lng)
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return {
        "message": "City added Successfully", 
        "city": new_city
    }