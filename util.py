from datetime import datetime


def parse_json_flights(data):

    data = data.json()

    legs = data['legs']
    fares = data['fares']

    price = fares[0]['price']['amount']
    airline_code = legs[0]['airlineCodes'][0]
    flight = legs[0]['segments'][0]['designatorCode']

    arrival_city = legs[0]['arrivalAirportCode']
    dep_city = legs[0]['departureAirportCode']
    stops = legs[0]['stopoversCount']

    departure_time = legs[0]['departureDateTime']

    target_date = datetime.fromisoformat(departure_time[0:19])

    current_date = datetime.now()

    difference = target_date - current_date

    days_left = difference.days

    tmp = departure_time[11:13]

    print(tmp)
    tmp = int(tmp)

    if (tmp > 4) & (tmp < 6):
        departure_time = "Early_Morning"
    elif (tmp >= 6) & (tmp <= 12):
        departure_time = "Morning"
    elif (tmp > 12) & (tmp < 22):
        departure_time = "Afternoon"
    else:
        departure_time = "Night"

    arrival_time = legs[0]['arrivalDateTime']

    tmp_other = arrival_time[11:13]
    tmp_other = int(tmp_other)

    if (tmp_other > 4) & (tmp_other < 6):
        arrival_time = "Early_Morning"
    elif (tmp_other >= 6) & (tmp_other <= 12):
        arrival_time = "Morning"
    elif (tmp_other > 12) & (tmp_other < 22):
        arrival_time = "Afternoon"
    else:
        arrival_time = "Night"

    cabin_class = 'Economy'
    duration = legs[0]['durationDays']
    duration = duration * 24

    resp = [airline_code, flight, dep_city, departure_time, stops, arrival_time, arrival_city, cabin_class,
            duration, days_left, 91 * price]

    return resp
