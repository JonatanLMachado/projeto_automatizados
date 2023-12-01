from OnlinePaymentService import OnlinePaymentService

class PaypalService(OnlinePaymentService):
    FEE_PERCENTAGE = 0.02
    MONTHLY_INTEREST = 0.03

    def payment_fee(self, amount):
        return amount * self.FEE_PERCENTAGE

    def interest(self, amount, months):
        return amount * self.MONTHLY_INTEREST * months
