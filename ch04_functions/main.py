'''
### 함수의 종류
1. 파이썬 내장 함수
2. 메서드
3. 사용자 정의 함수

### 함수 용어 정리
1. 함수 정의 : 사용자 정의 함수를 새로 만드는 것
2. 인수 : 함수에 전달할 입력값
3. 매개변수 : 매개변수로 받아서 저장하는 변수
4. 리턴값 : 함수의 출력값
5. 함수 호출 : 함수를 실제로 사용하는 것

### 사용자 정의 함수
1. 함수 정의 부분
함수_이름(매개변수1, 매개변수2):
    실행문
    return ...
2. 함수 호출 부분
변수 = 함수_이름(매개변수1, 매개변수2)
'''

# eng_name = input('당신의 이름을 영어로 입력하세요. >>> ')
# eng_name_low = eng_name.lower()
# eng_name_up = eng_name.upper()
#
# print(f"{eng_name_low}, {eng_name_up}" )

'''
str 자료형에 있는 .함수명()으로 호출함
여기서 중요한게 함수는 독립적으로 사용 가능하고 특정 클래스에 있는 함수들을 메서드라고 함
'''

# def multiply(n):
#     for i in range(1,10):
#         print(f"{n} X {i} = {n*i}")
#
# dan = int(input("몇 단을 출력하시겠습니까? >>> "))
# multiply(dan)

'''
파이썬에만 있는 연산자
** 제곱
// 몫

'''
#
# print(5%2)
# print(5//2)

def vending_machine(money):
    i = 0
    while money >= 700:
        print(f"음료수 = {i}개, 잔돈 = {money}원")
        i += 1
        money -= 700
    print(f"음료수 = {i}개, 잔돈 = {money}원")

vending_machine(3000)