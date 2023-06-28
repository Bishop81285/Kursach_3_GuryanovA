from pathlib import Path

USE_LOCAL_DATA = True
ROOT_PATH = Path().resolve().parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
DATA_JSON = Path.joinpath(DATA_PATH, 'operations.json')
DATA_JSON_TEST = Path.joinpath(DATA_PATH, 'data_test.json')
