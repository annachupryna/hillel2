import pytest
import requests

BASE_URL = "http://127.0.0.1:8080"

cars_db = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    6: {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    7: {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    8: {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    9: {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    10: {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    11: {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    12: {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    13: {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    14: {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    15: {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    16: {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    17: {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    18: {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    19: {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    20: {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    21: {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    22: {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    23: {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    24: {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    25: {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
}


def sort_cars_by_field(cars, field):
    def get_sort_key(car):
        return car[field]

    sorted_cars = sorted(cars, key=get_sort_key)
    return sorted_cars


@pytest.mark.parametrize("sort_by, limit, expected_result", [
    ("brand", 2, sort_cars_by_field(list(cars_db.values()), "brand")[:2]),
    ("year", 3, sort_cars_by_field(list(cars_db.values()), "year")[:3]),
    ("price", 1, sort_cars_by_field(list(cars_db.values()), "price")[:1]),
    ("engine_volume", 4, sort_cars_by_field(list(cars_db.values()), "engine_volume")[:4])
])
def test_get_cars(auth_token, sort_by, limit, expected_result):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.get(f'{BASE_URL}/cars', headers=headers, params=params)

    assert response.status_code == 200, f'Request failed, 200 expected but {response.status_code} received'

    assert response.json() == expected_result, f'Expected and received data do not match'
