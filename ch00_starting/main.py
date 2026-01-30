hello = '''
'''

# print(hello)

print('1')
print(1+2)
print('1' + '2')
print(type(1))
print(type(1.1))
# print() : 콘솔에 출력하는 함수
# type() : 매개변수가 어떤 자료형인지 알려주는 함수
print("end=라는 구문을 사용하면", end = ' / ')
print('끝에 나오는 부분을 통제할 수 있음')

name = '김영'
age = 20
print('안녕하세요. 제 이름은' +  name +'이고, 나이는 '+  str(age) +'살입니다.')
print(f'안녕하세요. 제 이름은 {name}이고, 나이는 {age+1}살입니다.')

# name2 = input("이름을 입력하세요 >>> ")
# print(name2)
age2 = input('나이를 입력하세요 >>> ')
print(type(age2))