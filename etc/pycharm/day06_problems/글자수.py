import sys
sys.stdin = open("글자수_input.txt")

T = int(input())
for _ in range(T):
    pattern = input()
    text = input()

    letter = {}  ## 딕셔너리 초기화
    for i in set(pattern): # set으로 중복값 빼준 후 딕셔너리에 초기화
        letter[i] = 0

    for i in text:  #text값이 없으면 넘어가고 있다면 딕셔너리 증가
        if letter.get(i) == None:
            continue
        letter[i]+=1

    imax = -1  # 완성된 딕셔너리에서 최대값 출력
    for i in letter.values():
        if i > imax:
            imax = i
    print(f"#{_+1} {imax}")  # 프린트