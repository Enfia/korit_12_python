# 파이썬은 향상된 for문이 기본 for문이다
# range() 함수가 중요함

# in이 연산자임
for i in range(10):
    print(i+1, end=" ")

print()
# range(시작값, 한계값, 증감값) 시험에 나옴
# 시작값과 증감값 생략 가능
for asd in range(2, 11, 2):
    print(asd)
print("마지막 값:", asd)


nums = [1,2,3,4,5]
for i in nums:
    print(i, end = " ")

print()
if 5 in nums:
    print('5가 nums 리스트 안에 있습니다.')
else:
    print('5가 nums 리스트 안에 없습니다')

print(5 in nums) # 결과값 : True