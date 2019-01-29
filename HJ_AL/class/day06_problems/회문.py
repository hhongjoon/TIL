import sys
sys.stdin = open("회문_input.txt")
def getresult(data):##
    # 가로먼저
    for j in range(size):
        for jj in range(size-pattern_size+1):         # 전체 길이 - 패턴길이 만큼 실행
            temp = data[j][jj:jj + pattern_size]    # slice를 통해 패턴길이만큼 자름
            #print(temp)
            if temp == temp[::-1]:                  # 역순이 일치하면 return
                return "".join(temp)
    #세로
    for col in range(size):
        for row in range(size-pattern_size+1):   # 전체 길이 - 패턴길이 만큼 실행
            result = ""
            count = 0
            while count<pattern_size:          # 슬라이스 할 수 없으므로 임시값에 한 문자씩 추가  / 최대 패턴길이 만큼 실행. 다 만들어 놓고 비교 brutforce한 방법
                result += data[row+count][col]
                count +=1
                #print(result)
            if result == result[::-1]:        # 일치하는지 확인
                return "".join(result)

# 실행부 ======================================

T = int(input())

for _ in range(T):
    size, pattern_size = map(int, input().split())
    data = []
    for i in range(size):
        data.append(list(map(str,input())))
    print(f"#{_+1}",end=" ")
    print(getresult(data))

