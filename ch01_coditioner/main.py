# 들여쓰기 중요함

# age = int(input('나이를 입력하세요 >>> '))
# if age > 20:
#     print('성인입니다.')
# elif age <= 20 and age > 13:
#     print('청소년입니다.')
# else:
#     print('어린이입니다.')

age = 21
has_ticket = True
print(type(has_ticket))
if age >= 19:
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요.')
else:
    print('미성년자는 출입할 수 없습니다')

# 비교 연산자 자바랑 똑같음
'''
논리 연산자

and : &&
or : ||
not : !=
'''
