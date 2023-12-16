from util import parse_json_flights
from fastapi import FastAPI, HTTPException
import uvicorn
from db.models import ApiRequest
from db.database import add_flight
from req.getFlight import get_flight

app = FastAPI()


@app.get("/getFlight")
def get_flight_endpoint(flight: ApiRequest):
    try:
        res = get_flight(flight)

        data = parse_json_flights(res)

        add_flight(data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    finally:

        return {"airline_code": data[0],
                "flight": data[1],
                "departure_city": data[2],
                "departure_time": data[3],
                "stops": data[4],
                "arrival_time": data[5],
                "arrival_cty": data[6],
                "cabin_class": data[7],
                "duration": data[8],
                "days_left": data[9],
                "price": data[10]
                }


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)