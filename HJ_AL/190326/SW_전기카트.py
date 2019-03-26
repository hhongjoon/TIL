import sys
sys.stdin = open('전기카트.txt')

def cal_min(n,k,dis,path):
    global mindis
    if dis>mindis: return

    if n == k:
        plus = mat[path[-1]][0]
        if mindis>dis+plus:
            mindis = dis + plus
        # print(path, dis+plus)
        return
    else:
        for i in range(size):
            if i in path:
                continue
            plus = mat[path[-1]][i]
            tempP = path[:]
            tempP.append(i)
            cal_min(n,k+1,dis+plus,tempP)

    pass
T = int(input())
for _ in range(T):
    global size
    size=int(input())
    mat = [ list(map(int,input().split())) for i in range(size) ]
    mindis = 999999999
    cal_min(size,1,0,[0])
    print("#{} {}".format(_+1,mindis))