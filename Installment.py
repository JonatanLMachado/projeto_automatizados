class Installment:
    def __init__(self, due_date, amount):
        self.__due_date = due_date
        self.__amount = amount

    def get_due_date(self):
        return self.__due_date

    def set_due_date(self, due_date):
        self.__due_date = due_date

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount
