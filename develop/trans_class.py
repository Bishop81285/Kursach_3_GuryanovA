class Transactions:
    def __init__(self, **kwargs):
        self._id: int = kwargs['id']
        self.state: str = kwargs['state']
        self.date: str = kwargs['date']
        self.amount: str = kwargs['operationAmount']['amount']
        self.currency: str = kwargs['operationAmount']['currency']['name']
        self.description: str = kwargs['description']
        self._from: str = kwargs['from']
        self.to: str = kwargs['to']

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'
