from OnlinePaymentService import OnlinePaymentService

class PicpayService(OnlinePaymentService):
    FEE_PERCENTAGE = 0.01
    MONTHLY_INTEREST = 0.04

    def payment_fee(self, amount):
        return amount * self.FEE_PERCENTAGE

    def interest(self, amount, months):
        return amount * self.MONTHLY_INTEREST * months
