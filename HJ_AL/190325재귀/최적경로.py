import time

def perm(n,k,dis,prev):
    global mindis
    # print(n,k)
    if dis >=mindis:
        return

    global total
    total += 1

    if n == k:
        # print(dis)
        dis += abs(goal[0] - prev[0]) + abs(goal[1] - prev[1])
        if mindis > dis:
            mindis = dis
        return
    else:
        for i in range(k,n):
            guests[i],guests[k] = guests[k],guests[i]
            # print(guests[k], prev)
            plus = abs(guests[k][0] - prev[0]) + abs(guests[k][1] - prev[1])
            perm(n,k+1,dis+plus,guests[k])
            guests[i], guests[k] = guests[k], guests[i]



T = int(input())
stime = time.time()
for _ in range(T):
    N = int(input())
    datas = list(map(int,input().split()))
    idx = [0]*N
    guests=[]
    for i in range(0,len(datas),2):
        guests.append((datas[i], datas[i+1]))
    st = guests.pop(0)
    goal = guests.pop(0)
    # print(guests, st, goal)
    total = 0
    mindis = 999999999999999999999999
    perm(N,0,0,st)
    print(mindis,'최소')
    print(total,'횟수')

etime = time.time()
print(etime-stime,'초')