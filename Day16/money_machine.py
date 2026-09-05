class MoneyMachine:

    CURRENCY = "$"

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")

        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickles?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01

        return total

    def make_payment(self, cost):
        payment = self.process_coins()

        if payment >= cost:
            change = round(payment - cost, 2)

            print(f"Here is ${change} in change.")

            self.profit += cost
            return True

        print("Sorry, that's not enough money. Money refunded.")
        return False
