class Person:
    name ='나다'
    def __init__(self):
        print(f'응애 {self.name}')
    def __del__(self):
        print('bye')



pp = Person()
