
def bfs(st,goal,cnt):
    Q =[]

    Q.append((st,cnt))
    while len(Q)>0:
        temp = Q.pop(0)
        val = temp[0]
        cnt = temp[1]

        if val == goal:
            return cnt


        if not visited[val+1]:
            if val + 1 < 1000000:
                Q.append((val+1,cnt+1))
                visited[val+1] = 1
        if not visited[val - 1]:
            if val - 1 > 0:
                Q.append((val-1,cnt+1))
                visited[val - 1] = 1
        if not visited[val *2]:
            if val *2 < 1000000:
                Q.append((val*2,cnt+1))
                visited[val*2] = 1
        if not visited[val - 10]:
            if val -10 >0:
                Q.append((val-10,cnt+1))
                visited[val - 10] = 1

T = int(input())
for _ in range(1,T+1):
    st,goal = map(int,input().split())
    visited = [0] * 999999
    res = bfs(st,goal,0)
    print("#{} {}".format(_,res))
