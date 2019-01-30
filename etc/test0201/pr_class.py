#1
# class Person:
#     pass
#
# p = Person()
# print(p)


#2
class Person:
    name = "고길동"
    def sayhello(self):
        print(f"안녕 나는 {self.name}")

aa = Person()
aa.sayhello()
aa.name = '홍준'  ## 여기서 바뀌었기 떄문
aa.sayhello()

#풀어서 쓸 때
Person.sayhello(aa)  # 첫자리는 self
print(isinstance(aa, Person))

