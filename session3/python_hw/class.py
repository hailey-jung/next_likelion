class Person:
    def __init__(self,name,age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}입니다. 제 나이는 {self.age}살 입니다. 제 키는 {self.height}입니다.")
        
    def yell(self):
        print("아?")

class Developer (Person):
    keyboard = '기계식'
    def __init__(self,name,age, height):
        super().__init__(name,age, height)

def yell (self):
    print("어?")

class Designer (Person):
    def __init__(self,name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager (Person):
    def __init__(self,name, age, height):
        super().__init__(name, age, height)

    def aging(self):
        self.age +=2
        self.height -=5
        print("개발자를 새로 뽑아야하나...")
        Developer.keyboard ='엠브레인'

    def yell(self):
        print("개발자님 여기 오류있어요")

d1=Developer('정효진', 22, 162)
d2=Designer('김그림', 24, 170, '복통')
p1=ProductManager('김부장', 29, 170)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()

