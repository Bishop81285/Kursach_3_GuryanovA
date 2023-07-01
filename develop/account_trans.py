from develop.utils import get_data, show_last_trans


def main():
    data: list[dict] = get_data()

    show_last_trans(data)


if __name__ == '__main__':
    main()
