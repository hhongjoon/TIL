# 선생님코드
# 1-100점까지 리스트를 만들고 점수별로 카운트
# 조건에 맞게끔 집어 넣음
# 리스트 나올 때마다 차이 값 계산하여 산출

def isbreak(x,kmin,kmax):   # 범위 값
    if len(x) < kmin or len(x) > kmax:
        return True
    return False

def cal_room(kmin,kmax,T):  # 조건에 맞추어 해당하는 리스트 들을 뽑아냄
    result = []
    for i in range(T-1):
        a = data[:i]
        if isbreak(a,kmin,kmax):
            continue
        for j in range(i+1,T):
            b = data[i:j]
            if isbreak(b,kmin,kmax):
                continue
            if len(set(a) & set(b))  > 0: #중복값 존재
                break # for 하나만 탈출

            c = data[j:]
            if isbreak(c,kmin,kmax):
                continue
            if len(set(b) & set(c)) > 0:  # 중복값 존재
                continue  # for 하나만 탈출

            print(a,b,c)
            temp = []
            temp.append(a)
            temp.append(b)
            temp.append(c)
            result.append(temp)
    return result

T = int(input())
for _ in range(T):
    N, kmin, kmax = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()
    room = [0]*3
    roomlist = cal_room(kmin,kmax,N)
    if len(roomlist) == 0:
        goal = -1
    else:
        finalL = []
        for i in range(len(roomlist)):
            roomlen = []
            for j in range(3):
                roomlen.append(len(roomlist[i][j]))
            roomlen.sort()
            temp = roomlen[-1] - roomlen[0]
            finalL.append(temp)
        goal = min(finalL)

    print(goal)












    # if len(roomlist) == 0:
    #     goal = -1
    #
    # elif len(roomlist) == 1:
    #     step1 = abs(len(roomlist[0][2]) - len(roomlist[0][1]))
    #     step2 = abs(len(roomlist[0][1]) - len(roomlist[0][0]))
    #     step3 = abs(len(roomlist[0][0]) - len(roomlist[0][2]))
    #     goal = max(step1,step2,step3)
    # else:
    #     finalL = []
    #     for i in range(len(roomlist)):
    #         step1 = abs(len(roomlist[i][2]) - len(roomlist[i][1]))
    #         step2 = abs(len(roomlist[i][1]) - len(roomlist[i][0]))
    #         step3 = abs(len(roomlist[i][0]) - len(roomlist[i][2]))
    #         goal = max(step1, step2, step3)
    #         finalL.append(goal)
    #     goal = min(finalL)
    #
    # print(goal)