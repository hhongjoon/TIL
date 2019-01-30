class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1  ## 생성될 떄마다 1
    def greeting(self):
        print(f"{self.name}입니다.")

    @staticmethod
    def paynow():
        print('스태틱')

p = Person('SHJ')  ## 어트리뷰트는 없지만 생성되면서 저장
print(p.name)


