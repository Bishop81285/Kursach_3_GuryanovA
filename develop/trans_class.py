from datetime import datetime


class Transactions:
    def __init__(self, **kwargs):
        self._id: int = kwargs['id']
        self.state: str = kwargs['state']
        self.date: str = kwargs['date']
        self.amount: str = kwargs['operationAmount']['amount']
        self.currency: str = kwargs['operationAmount']['currency']['name']
        self.description: str = kwargs['description']

        # Not all transactions contain the field "from"
        if 'from' in kwargs:
            self._from: str = kwargs['from']
        else:
            self._from: str = ''

        self.to: str = kwargs['to']

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

    def convert_date(self):
        """
        Converts date to standard format ДД.ММ.ГГГГ
        :return: converted date string
        """
        date = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        return date.strftime('%d.%m.%Y')

    @staticmethod
    def details_masked(details: list[str]) -> str:
        if "Счет" in details:
            short_account = details[0] + ' ' + '**' + details[1][-4:]
            return short_account
        else:
            if len(details) == 3:
                short_card = details[0] + ' ' + details[1] + ' ' + details[2][:4] + ' ' + \
                                  details[2][4:6] + '**' + ' ' + '****' + ' ' + details[2][-4:]
                return short_card
            else:
                short_card = details[0] + ' ' + details[1][:4] + ' ' + \
                                  details[1][4:6] + '**' + ' ' + '****' + ' ' + details[1][-4:]
                return short_card

    def convert_details(self) -> tuple[str, str]:
        """
        Converts card and account details to masked format with "*"
        :return: tuple of converted details (from, to)
        """
        _from_sep = self._from.split()
        _to_sep = self.to.split()

        if not self._from:
            short_account = _to_sep[0] + ' ' + '**' + _to_sep[1][-4:]
            return '', short_account
        else:
            return self.details_masked(_from_sep), self.details_masked(_to_sep)

    def view_trans(self) -> str:
        """
        Makes right format for transaction view:
        <дата перевода> <описание перевода>
        <откуда> -> <куда>
        <сумма перевода> <валюта>
        :return: formatted string of transaction
        """
        date_line = self.convert_date()
        from_details, to_details = self.convert_details()

        line_1 = " ".join([date_line, self.description])
        line_2 = " -> ".join([from_details, to_details]) if from_details else "-> " + to_details
        line_3 = " ".join([self.amount, self.currency])

        return line_1 + '\n' + line_2 + '\n' + line_3
