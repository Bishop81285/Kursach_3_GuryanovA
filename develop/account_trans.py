from develop.trans_class import Transactions
from develop.utils import get_data


def main():
    data: list[dict] = get_data()
    asf = data[0]

    trans1 = Transactions(**asf)
    print(trans1)


if __name__ == '__main__':
    main()
