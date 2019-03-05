T = int(input())
for _ in range(T):
    ea, goal = map(int,input().split())
    temp = list(map(int,input().split()))
    tree = []
    for i in range(ea):
        tree.append((temp[i*2],temp[i*2+1]))

    print(tree)
    # process
    visit =[]
    visit.append(goal)
    result = []
    while len(visit)>0:
        a = visit.pop()
        if a not in result:
            result.append(a)
        for i in range(len(tree)):
            if tree[i][0] == a:
                visit.append(tree[i][1])

    # print(f"#{_ + 1} {len(result)}")