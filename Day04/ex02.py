'''
    클래스 선언

    class 클래스명:
        클래스 내용 (생성자, 소멸자, 메소드)

        # 생성자
        # : 객체가 생성될 때, 실행되는 메소드
        def __init__(self, 매개변수):
            생성자 내용
            
        # self : 객체 자신을 가르키는 키워드(딕셔너리)
        # self.(변수), self.(매소드)

        # 소멸자
        # : 객체가 소멸될 때, 실행되는 메소드
        def __del__(self):
            생성자 내용
        
        # 메소드
        # : 클래스 내에서 정의된 함수
        def 메소드명(self, 매개변수):
            메소드 내용
'''

# Person 클래스 선언
class Person:
    
    # 생성자
    # def __init__(self):
    #     print('Person 객체 생성...')

    def __init__(self, name=None, age=None, tel=None):
        self.name = name
        self.age = age
        self.tel = tel
        print('Person 객체 생성...')
        
    # 소멸자
    def __del__(self):
        print('Person 객체 소멸...')

        
    # 메소드
    def show_info(self):
        print('이름 : {}, 나이 : {}, 전화번호 : {}'
              .format(self.name, self.age, self.tel))
# class Person 끝


# Person 객체 생성
person = Person()

# 객체의 변수 접근
person.name = '김휴먼'
person.age = 20
person.tel = '010-1234-1234'

print('이름 : ',person.name)
print('나이 : ',person.age)
print('전화번호 : ',person.tel)


person2 = Person('이휴먼', 20, '010-1212-3434')
print('이름 : ',person2.name)
print('나이 : ',person2.age)
print('전화번호 : ',person2.tel)
    
        
person3 = Person('박휴먼', 30, '010-5656-9999')
person3.show_info()


p = Person(name='aaa')
p.show_info


class Board:
    def __init__(self, title=None, writer=None, content=None):
        self.title = title
        self.writer = writer
        self.content = content
        
    def show_info(self):
        print('제목 : {} \n작성자 : {} \n내용 : {}'
              .format(self.title, self.writer, self.content))

board = Board('아브라카다브라'
            , '김휴먼'
            , '벚꽃은 오래 피지 않는다.')
board.show_info()


class Gallery(Board):
    def __init__(self, title, writer, content, image):
        super().__init__(title, writer, content)
        self.image = image
        
    def show_info(self):
        print('제목 : {} \n작성자 : {} \n내용 : {} \n이미지 : {}'
              .format(self.title, self.writer, self.content, self.image))
        
gallery = Gallery('아브라카다브라'
                , '김휴먼'
                , '벚꽃은 오래 피지 않는다.'
                , 'https://i.imgur.com/CbuD3gl.png')
gallery.show_info()
    
