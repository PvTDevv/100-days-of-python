from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

keep_working = True
while keep_working:
    costumer_request = input(f"What would you like? ({menu.get_items()}): ").lower()

    if costumer_request == "off":
        keep_working = False
        continue

    elif costumer_request == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(costumer_request)

    if drink:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
