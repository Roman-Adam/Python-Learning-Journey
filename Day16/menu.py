class MenuItem:

    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(
                name="espresso",
                cost=1.5,
                ingredients={
                    "water": 50,
                    "coffee": 18,
                },
            ),
            MenuItem(
                name="latte",
                cost=2.5,
                ingredients={
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            ),
            MenuItem(
                name="cappuccino",
                cost=3.0,
                ingredients={
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            ),
        ]

    def get_items(self):
        menu = ""

        for item in self.menu:
            menu += f"{item.name}/"

        return menu

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item

        print("Sorry, that item is not available.")
        return None
