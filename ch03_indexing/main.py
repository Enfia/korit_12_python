str_example = 'Hello, Python!'

for i in range(len(str_example)):
    print(str_example[i], end= "")

print()

for i in str_example:
    print(i, end = "")

print()
'''
변수명[시작인덱스 : 종료인덱스 : 증감값]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 증가함
'''
# 예시)
# print(str_example[-6])

k = input("네 자리 숫자를 입력하세요 >>> ")

if len(k) == 4:
    if int(k) % 2 == 0:
        print("맨 마지막 숫자는 " + k[-1] + "이며 짝수입니다.")
    else :
        print("맨 마지막 숫자는 " + k[-1] + "이며 홀수입니다.")
else:
    print("네 자리 숫자를 입력해주세요.")
'''
파이썬 삼항 연산자
if - else 구조를 한 줄로 줄여 써보자 ^^
'''
result = '짝수' if int(k[-1]) % 2 == 0 else '홀수'

print(f'맨 마지막 숫자는 {k[-1]}이며 {result}입니다.')