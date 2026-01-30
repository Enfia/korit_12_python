# 1부터 10까지 출력하기
# 파이썬에는 i++ 가 없음
# n = 1
# while n < 11:
#     print(n, end=" ")
#     n += 1
#
# print()
# n2 = 10
# while n2 > 0:
#     print(n2, end=" ")
#     n2 -= 1
dan = 2
while dan < 10:
    number = 1

    while number < 10:
        print(f"{dan} X {number} = {dan*number}")
        number += 1
    dan += 1