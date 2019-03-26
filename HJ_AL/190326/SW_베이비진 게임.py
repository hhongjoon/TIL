import sys
sys.stdin = open('베이비진.txt')

def cal(idx):
    if idx.count(3):
        return 1
    leng=0
    for i in range(len(idx)):
        if idx[i] == 0:
            leng = 0
            continue
        else:
            leng+=1
            if leng == 3:
                return 1
    return 0

T = int(input())
for _ in range(T):
    datas = list(map(int,input().split()))
    A=[]
    B=[]
    for i in range(len(datas)):
        if i%2==0:
            A.append(datas[i])
        else:
            B.append(datas[i])
    idxA=[0]*10
    idxB=[0]*10
    result=0
    while A and B:
        idxA[A.pop(0)] += 1
        r_a = cal(idxA)
        if r_a:
            result = 1
            break
        idxB[B.pop(0)] += 1
        r_b = cal(idxB)
        if r_b:
            result = 2
            break
    print("#{} {}".format(_+1,result))

