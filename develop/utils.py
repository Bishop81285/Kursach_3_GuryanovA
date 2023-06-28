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


def show_last_executed_trans(data_trans: list[dict], amount: int = 5) -> None:
    """
    Show last 'amount' transactions that were executed
    :param data_trans: python-json format data
    :param amount: number of transactions
    :return: nothing, just printing
    """
    executed_trans = [el for el in data_trans if 'state' in el and el['state'] == 'EXECUTED']

    if amount > len(executed_trans):
        print(f'AmountError: set correct amount of transactions (< {len(executed_trans) + 1})')
        return

    executed_trans_date_sorted = sorted(executed_trans, key=lambda el: el['date'], reverse=True)

    executed_trans_view = []

    for i in range(amount):
        executed_trans_view.append(Transactions(**executed_trans_date_sorted[i]))

    print('EXECUTED:')

    for trans in executed_trans_view:
        print(trans.view_trans())
        print('')


def show_last_canceled_trans(data_trans: list[dict], amount: int = 5) -> None:
    """
    Show last 'amount' transactions that were canceled
    :param data_trans: python-json format data
    :param amount: number of transactions
    :return: nothing, just printing
    """
    canceled_trans = [el for el in data_trans if 'state' in el and el['state'] == 'CANCELED']

    if amount > len(canceled_trans):
        print(f'AmountError: set correct amount of transactions (< {len(canceled_trans) + 1})')
        return

    canceled_trans_date_sorted = sorted(canceled_trans, key=lambda el: el['date'], reverse=True)

    canceled_trans_view = []

    for i in range(amount):
        canceled_trans_view.append(Transactions(**canceled_trans_date_sorted[i]))

    print('CANCELED:')

    for trans in canceled_trans_view:
        print(trans.view_trans())
        print('')
