import sys
sys.stdin = open("문자열비교_input.txt")

T = int(input())
for _ in range(T):
    pattern = input()
    text = input()
    i = 0           # text의 자리값
    j = 0           # pattern의 자리값
    print(f"#{_+1}", end=" ")
    # if len(pattern)>len(text):
    #     print(0)
    #     break
    while i<len(text) and j<len(pattern):
        if pattern[j] != text[i]:  # 같지 않으면
            i = i-j                # i = i-j를 통해서 시작값을 바꿔줌
            j = -1
        i = i+1
        j = j+1

    if j == len(pattern):
        print(1)
    else:
        print(0)
