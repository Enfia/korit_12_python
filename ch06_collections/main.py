'''
파이썬 대표 콜렉션 종류
1. 리스트 : 추가 / 수정 / 삭제 가능 / 순서 있음
2. 튜플 : 추가 / 수정 / 삭제 불가능 / 순서 있음
3. 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. 딕셔너리 : 키 + 값으로 관리
'''
list_example = [30, 40, '김이', [100, '김삼']]
print(list_example[3][0])

tuple_example = (10, 20, 30, '김사')
print(tuple_example)
set_example = {100, 200, 300, 400, '김오'}
print(set_example)
dict_example = {'이름':'김일', '나이':20, '학교': '코리아아이티'}
print(dict_example)