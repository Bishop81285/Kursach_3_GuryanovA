import json

from cfg.settings import DATA_JSON
from develop.trans_class import Transactions


def get_data() -> list[dict]:
    """
    Get json data from file and convert to python format
    :return: python-json data
    """
    _path = DATA_JSON

    with open(_path) as file:
        return json.load(file)


def show_last_executed_trans(data_trans: list[dict], amount: int = 5) -> None:
    executed_trans = [el for el in data_trans if 'state' in el and el['state'] == 'EXECUTED']
    executed_trans_date_sorted = sorted(executed_trans, key=lambda el: el['date'], reverse=True)

    executed_trans_view = []

    for i in range(amount):
        executed_trans_view.append(Transactions(**executed_trans_date_sorted[i]))

    for trans in executed_trans_view:
        pass

