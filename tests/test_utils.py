import json

from develop.utils import get_data, show_last_executed_trans, show_last_canceled_trans


def test__get_data(json_data: tuple, faker):
    result: list[dict] = json.loads(get_data(json_data[0]))

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["Name"] == json_data[1]
    assert result[1]["Age"] == json_data[2]


def test__show_last_executed_trans(json_trans_executed: list[dict], capsys):
    show_last_executed_trans(json_trans_executed, 1)

    captured = capsys.readouterr()

    expected_output = """EXECUTED:\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб.\n\n"""

    assert expected_output == captured.out

    show_last_executed_trans(json_trans_executed, 3)
    captured = capsys.readouterr()

    expected_output = f'AmountError: set correct amount of transactions (< {len(json_trans_executed) + 1})\n'

    assert expected_output == captured.out


def test__show_last_canceled_trans(json_trans_canceled: list[dict], capsys):
    show_last_canceled_trans(json_trans_canceled, 1)

    captured = capsys.readouterr()

    expected_output = """CANCELED:\n12.09.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657
67314.70 руб.\n\n"""

    assert expected_output == captured.out

    show_last_canceled_trans(json_trans_canceled, 3)
    captured = capsys.readouterr()

    expected_output = f'AmountError: set correct amount of transactions (< {len(json_trans_canceled) + 1})\n'

    assert expected_output == captured.out


def test__show_last_trans_no_from(json_trans_nofrom, capsys):
    show_last_executed_trans(json_trans_nofrom, 1)

    captured = capsys.readouterr()

    expected_output = """EXECUTED:\n28.12.2018 Открытие вклада\n-> Счет **2391\n49192.52 USD\n\n"""

    assert expected_output == captured.out
