from payment_method import PaymentMethod

class CreditcardPayment(PaymentMethod):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self,amount):
        print(f"Processing credit card number ${amount} for {self.card_holder}")

    def refund(self,amount):
        print(f"Refunding ${amount} to {self.card_holder}'s credit card.")

def process_transaction(paymentMethod: PaymentMethod,amount):
    paymentMethod.pay(amount)
    paymentMethod.refund(amount/2)
creditCard = CreditcardPayment("2343342-34233","kevin")
process_transaction(creditCard,1000)