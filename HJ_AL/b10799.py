aa = input()
size = []
piece = 0
for i in range(len(aa)):
    if aa[i] == '(':
        size.append('(')
    else:
        if aa[i-1] == '(':  # 레이저라면  # 칸을 나누었을 때 앞에 있는 '(' 갯수로 판단
            size.pop()
            piece += len(size)
        else:               # 레이저 아닐 때 , 괄호를 닫으면서 1개 생김 (규칙)
            size.pop()
            piece += 1
print(piece)