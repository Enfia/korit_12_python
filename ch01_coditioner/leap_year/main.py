year = int(input('연도를 입력하세요 >>> '))



if year < 0:
    print("불가능한 연도 입력입니다.")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년입니다.")
else :
    print("윤년이 아닙니다")