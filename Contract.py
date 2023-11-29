from datetime import date
from typing import List

class Contract:
    def __init__(self, number, date, total_value):
        self.__number = number
        self.__date = date
        self.__total_value = total_value
        self.__installments = []

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_total_value(self):
        return self.__total_value

    def set_total_value(self, total_value):
        self.__total_value = total_value

    def get_installments(self):
        return self.__installments

    def add_installment(self, installment):
        self.__installments.append(installment)
