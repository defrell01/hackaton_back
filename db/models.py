from pydantic import BaseModel


class ApiRequest(BaseModel):
    departureCode: str
    arrivalCode: str
    date: str
    numberOfAdults: int
    cabinClass: str


class PredictData(BaseModel):
    airline: str
    flight: str
    source_city: str
    departure_time: str
    stop: str
    arrival_time: str
    destination_city: str
    class_flight: str
    duration: float
    days_left: int
