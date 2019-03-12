def find_rotate(num):
    goal = path[num]
    if goal in visited:
        return True
    visited.append(goal)
    find_rotate(goal)



T = int(input())
for _ in range(T):
    N = int(input())
    order = list(map(int,input().split()))
    path={}
    for i in range(len(order)):
        path[i+1] = order[i]

    visited = []
    cnt=0
    for i in range(1,N+1):
        if i in visited:
            continue
        visited.append(i)
        if path[i] == i:
            cnt+=1
        else:
            find_rotate(i)
            cnt+=1
    print(cnt)

