import A

print("top-level B.py")
A.func()         ##A안에 있는 함수 가져옴


if __name__ == "__main__":
    print('B.py 직접실행')
else:
    print('B.py가 import 되어 사용됨')