class Request:
    def __init__(self, amount, product, to, from_):
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product


    def __str__(self):
        return print(f'Доставить {self.amount} {self.product} из {self.from_} в {self.to}')
