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
    elif choice in [item.name for item in menu.menu]:
        drink = menu.find_drink(choice)
        if drink is not None:
            continue
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print('ㄴㄴ')

    else:
        print('잘못 입력했습니다')