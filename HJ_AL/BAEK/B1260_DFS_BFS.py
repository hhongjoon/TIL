def dfs(root):
    visited=[]
    temp=[]
    temp.append(root)
    while len(temp) > 0:
        val = temp.pop()
        if val not in visited:
            print(val, end=" ")
            visited.append(val)
            if path.get(val) is None:
                continue
            temp+=path[val][::-1]

def bfs(root):
    visited = []
    temp = []
    temp.append(root)
    while len(temp) >0:
        val = temp.pop(0)
        if val not in visited:
            print(val,end=" ")
            visited.append(val)
            if path.get(val) is None:
                continue
            temp +=path[val]

    pass

N, M, root = map(int,input().split())
path = {}
# 양방향
for i in range(1,N+1):
    path[i]=[]
for i in range(M):
    start, goal = map(int,input().split())
    path[start].append(goal)
    path[goal].append(start)
for i in path.keys():
    path[i].sort()

# print(path)
dfs(root)
print()
bfs(root)