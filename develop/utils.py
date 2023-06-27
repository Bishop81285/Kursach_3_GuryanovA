import json

from cfg.settings import DATA_JSON


def get_data() -> list[dict]:
    """
    Get json data from file and convert to python format
    :return: python-json data
    """
    _path = DATA_JSON

    with open(_path) as file:
        return json.load(file)
