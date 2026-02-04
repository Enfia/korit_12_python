'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB
'''
class USB:
    def __init__(self, capacity):
        self.capacity = capacity
        print('USB 객체가 생성되었습니다.')

    def get_info(self):
        print(f'{self.capacity}GB USB')

usb = USB(64)
usb.get_info()