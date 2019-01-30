class Person:
    name = '고길동'
    money = 100
    age = 20
    def sayhello(self, money, age):
        print(f"안녕하세요 나는{self.name}")
        print(f"내재산{money}")
        print(f"내나이{age}")

p = Person()
print(p.money)
print(p.age)
p.sayhello(500, 30)
print(p.money)
print(p.age)
