MENU = {
    '에스프레소': {
        '재료' : {
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    },
}
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}
profit = 0

def report():
    print(f'물 : {resources['물']} ml')
    print(f'우유 : {resources['우유']} ml')
    print(f'커피 : {resources['커피']} g')
    print(f'$ {profit}')

def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다. 🙌')
            return False
    return True

def process_coins():
    '''
    동전을 입력 받아 전체 금액을 반환하는 함수 call3() 유형
    :return: total
    '''
    total = 0.0
    # quarters / dimes / nickels / pennies
    total += int(input('쿼터 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.25
    total += int(input('다임 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.1
    total += int(input('니켈 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.05
    total += int(input('페니 동전을 몇 개 넣으시겠습니까? >>> ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    global profit
    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        print(f'잔돈 ${change}를 반환합니다.')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')

def make_coffee(drink_name, order_ingredients): # call2() 유형으로 정의
    # 재료 감하는 부분
    for item in order_ingredients:   # order_ingredients = drink['재료']
        resources[item] -= order_ingredients[item]
    # 커피 안내문구
    print(f'{drink_name}☕가 나왔습니다. 맛있게 드세요 !! ❤️')

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>> ')
    #todo - 1 : choice가 off라면 자판기가 종료되었습니다, 라고 출력하면서 반복 종료
    if choice == 'off':
        is_on = False
        print('자판기를 종료합니다. 🎈')
    #todo - 2 : choice가 report라면 물 : 어쩌고ml ~ 커피 : 어쩌고g / 돈 : $몇달러 라고 출력될 수 있도록 작성하시오. -> def report()를 call1() 유형으로 정의해서 함수만 호출하시오.
    elif choice == 'report':
        report()
    #todo - 3 : choice가 에스프레소 / 라떼 / 카푸치노에 해당된다면 실행문으로 다음단계로직 이라고 콘솔에 출력할 수 있도록 코드를 작성하시오.
    elif choice in ['에스프레소', '라떼', '카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received, drink['가격']):
                make_coffee(choice, drink['재료'])

    #todo - 4 : 오타 발생 시에 잘못입력하셨습니다를 콘솔에 출력하고 다음 반복으로 넘어갈 수 있도록 코드를 작성하시오.
    else:
        print('잘못 입력 하셨습니다. 😂')