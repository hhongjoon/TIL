def func():
    print("function A.py")

print(f"A의 __name__은 {__name__}") # 어디에서 무엇이 도는지
print('top-level A.py')

if __name__ == "__main__":
    print('A.py 직접실행')
else:
    print('A.py 가 import 되어 실행됨')



