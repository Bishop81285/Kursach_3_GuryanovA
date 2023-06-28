import json

import pytest

from cfg.settings import DATA_JSON_TEST


@pytest.fixture
def json_data(faker):
    """
    Makes json format data for get_data() func test using Faker package
    :param faker: faker fixture for creating data
    :return: tuple of file path and info for testing
    """
    data_json = faker.json(data_columns=[('Name', 'name'), ('Age', 'pyint', {'min_value': 20, 'max_value': 80})],
                           num_rows=2)
    json_file_path = DATA_JSON_TEST
    data_json_conv = json.loads(data_json)

    with open(json_file_path, 'w') as file:
        json.dump(data_json, file)

    return json_file_path, data_json_conv[0]['Name'], data_json_conv[1]['Age']


@pytest.fixture
def json_trans_executed():
    json_trans = [
        {
            "id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации", "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589"
        }
    ]

    return json_trans


@pytest.fixture
def json_trans_canceled():
    json_trans = [
        {
            "id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации", "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"
        }
    ]

    return json_trans


@pytest.fixture
def json_trans_nofrom():
    json_trans = [
        {
            "id": 172864002, "state": "EXECUTED", "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада", "to": "Счет 96231448929365202391"
        }
    ]

    return json_trans
