import sys
sys.stdin = open("회문2_input.txt")


def getresult(data, pattern_size):##
    # 가로먼저
    for j in range(100):
        for jj in range(100-pattern_size+1):         # 전체 길이 - 패턴길이 만큼 실행
            temp = data[j][jj:jj + pattern_size]    # slice를 통해 패턴길이만큼 자름
            #print(temp)
            if temp == temp[::-1]:                  # 역순이 일치하면 return
                return True
    #세로
    for col in range(100):
        for row in range(100-pattern_size+1):   # 전체 길이 - 패턴길이 만큼 실행
            result = ""
            count = 0
            while count<pattern_size:          # 슬라이스 할 수 없으므로 임시값에 한 문자씩 추가  / 최대 패턴길이 만큼 실행. 다 만들어 놓고 비교 brutforce한 방법
                result += data[row+count][col]
                count +=1
                #print(result)
            if result == result[::-1]:        # 일치하는지 확인
                return True
    return False

# 실행부 ======================================
for _ in range(10):
    nomean = input()
    data = []
    for i in range(100):
        data.append(list(map(str,input())))

    #print(data)
    print(f"#{_+1}",end=" ")

    max = 0
    for ii in range(1,51):
        if getresult(data,ii):
            max = ii
    print(max)