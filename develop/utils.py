import json

from cfg.settings import DATA_JSON
from develop.trans_class import Transactions


def get_data(_path: str = DATA_JSON) -> list[dict] | str:
    """
    Get json data from file and convert to python format
    :return: python-json data
    """
    with open(_path) as file:
        return json.load(file)


def show_last_trans(data_trans: list[dict], amount: int = 5, type_operation='EXECUTED') -> None:
    """
    Show last 'amount' transactions that were executed or canceled
    :param data_trans: python-json format data
    :param amount: number of transactions
    :param type_operation: chose what kind of transaction you want to view
    :return: nothing, just printing
    """
    _trans = [el for el in data_trans if 'state' in el and el['state'] == type_operation]

    if amount > len(_trans):
        print(f'AmountError: set correct amount of transactions (< {len(_trans) + 1})')
        return

    _trans_date_sorted = sorted(_trans, key=lambda el: el['date'], reverse=True)

    _trans_view = [Transactions(**el) for el in _trans_date_sorted[:amount]]

    print(f'{type_operation}:')

    for trans in _trans_view:
        print(trans.view_trans())
        print('')
