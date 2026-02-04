from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자로 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? >>> {menu.get_items()} ')
    # todo 1
    if choice == 'off':
        print('자판기가 종료됨')
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        print(drink.name)
        print(drink.water)
        print(drink.milk)
        print(drink.coffee)
        print(drink.cost)