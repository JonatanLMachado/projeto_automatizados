from datetime import date
from dateutil.relativedelta import relativedelta
from Installment import Installment

class ContractService:
    def __init__(self, online_payment_service):
        self.__online_payment_service = online_payment_service

    def process_contract(self, contract, months):
        for i in range(months):
            basic_quota = contract.get_total_value() / months
            interest_fee = basic_quota + self.__online_payment_service.interest(basic_quota, i + 1)
            amount = interest_fee + self.__online_payment_service.payment_fee(interest_fee)
            
            due_date = contract.get_date() + relativedelta(months=i+1)
            
            contract.add_installment(Installment(due_date, amount))
