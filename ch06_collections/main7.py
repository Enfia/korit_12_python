# 숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
# 문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.
#
# 함수 정의 : add_numbers()
# 매개 변수 : 정수 n
#
# 함수 호출
# add_numbers1(last_num)          # call2() 유형
# print(add_numbers2(last_num))   # call4() 유형
#
# 실행 예
# 숫자 몇 까지 입력하시겠습니까? >>> 10
# [1,2,3,4,5,6,7,8,9,10]
# [1,2,3,4,5,6,7,8,9,10]
#
# 예를 들어 hello = ['안', '녕', '하', '세', '요']라는 list가 있다고 가정했을 때,
# add_numbers3(10, hello)를 호출하면
# [1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
# 라는 결과값을 만드는 함수를 정의한다면 어떻게 할 수 있을지 고민해보세요.

last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))

def add_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    print(numbers)

def add_numbers2(n):
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    return numbers

def add_numbers3(n, k):
    num = len(k)
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    for i in range(num):
       numbers.append(k[i])
    print(numbers)


add_numbers(last_num)
print(add_numbers2(last_num))

hello = ['안', '녕', '하', '세', '요']
add_numbers3(10, hello)