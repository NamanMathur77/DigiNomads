from pydantic import BaseModel

class Coordinate(BaseModel):
    lat: float
    long: float

    def __init__(self, lat, long):
        super().__init__(lat = lat, long = long)