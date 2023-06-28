from develop.utils import get_data, show_last_executed_trans, show_last_canceled_trans


def main():
    data: list[dict] = get_data()

    show_last_executed_trans(data)
    # show_last_canceled_trans(data, 7)


if __name__ == '__main__':
    main()
