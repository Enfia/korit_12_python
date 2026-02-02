dict1 = {
    '1' : 31,
    '2' : 28,
    '3' : 31,
    '4' : 30,
    '5' : 31,
    '6' : 30,
    '7' : 31,
    '8' : 31,
    '9' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31,

}
month = input('1 ~ 12월 사이의 월을 입력하세요 >>> ')
print(f'{month}월은 {dict1[month]}일까지 입니다.')

list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(f'{month}월은 {list[(int(month)-1)]}일까지 입니다.')


list2 = [28,30,31]
if int(month) == 2:
    print(f'{month}월은 {list2[0]}일까지 입니다.')
elif int(month) in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
    print(f'{month}월은 {list2[2]}일까지 입니다.')
elif int(month) in [4 , 6 , 9 , 11]:
    print(f'{month}월은 30일까지 입니다.')