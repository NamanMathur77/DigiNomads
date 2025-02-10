from pydantic import BaseModel

class City(BaseModel):
    name: str
    lat: float
    lng: float
    population: int
    country: str
