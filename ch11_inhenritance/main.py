# 형식
# class 슈퍼클래스:
#     본문
# class 서브클래스(슈퍼클래스):
#     본문

class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이가 {food}를 먹습니다.')

    def drink(self, drink_name):
        print(f'{self.name}이가 {drink_name}을 먹습니다')

person1 = Person('김영')
person1.eat('감자')

class Student(Person):
    def __init__(self, name, school): # 생성자는 함수임
        super().__init__(name)
        self.school = school

    def study(self):
        print(f'{self.name}은 {self.school}에서 공부를 합니다.')

    def drink(self, drink_name):
        print(f'{self.school}에서 ', end= ' ')
        super().drink(drink_name)

potter = Student(name='해리포터', school='호그와트')
potter.study()
potter.eat('라멘') # 해리포터이가 라멘를 먹습니다.
potter.drink('아메리카노') # overriding된 함수를 호출

# 자식 클래스는 부모 클래스가 없으면 존재할 수 없음
# 부모 클래스에서 객체가 생성되어야 자식 클래스도 생성할 수 있음
# 별개의 인스턴스로 생성 된거냐? <<< 애매함

# 슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
# 서브 클래스의 인스턴스는 서브 클래스의 인스턴스고 동시에 슈퍼 클래스의 인스턴스

# isinstance(객체명, 클래스명) -> boolean
print(isinstance(potter, Student)) # True
print(isinstance(potter, Person)) # True
print(isinstance(person1, Student)) # False
print(isinstance(person1, Person)) # True
print(issubclass(Student, Person)) # True
print(issubclass(Person, Student)) # True
