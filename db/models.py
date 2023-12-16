from pydantic import BaseModel


class ApiRequest(BaseModel):
    departureCode: str
    arrivalCode: str
    date: str
    numberOfAdults: int
    cabinClass: str

