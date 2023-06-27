from pathlib import Path

USE_LOCAL_DATA = True
ROOT_PATH = Path().resolve().parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
DATA_JSON = Path.joinpath(DATA_PATH, 'operations.json')
