class Request:
    def __init__(self, from_, to, amount, product):
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product
        

    def request(self):
        return f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}'
