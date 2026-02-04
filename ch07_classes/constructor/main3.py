'''

응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오
man = Person('james')
woman = Person('emily')
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오
james is born.
emily is born.

3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

4. 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.
'''

class Person:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is born.')

    def __del__(self):
        print(f'{self.name} is dead.')

man = Person('james')
woman = Person('emily')

del man