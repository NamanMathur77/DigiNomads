from pydantic import BaseModel
from coordinate import Coordinate

class City(BaseModel):
    id: int
    name: str
    coordinate: Coordinate
    country: str
    population: int