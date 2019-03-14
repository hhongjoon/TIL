
def dfs(a):

    temp=[]

    temp.append(a)

    while len(temp)>0:
        num = temp.pop()
        if num in visited:
            continue
        else:
            visited.append(num)
            if mat.get(num) is not None:
                temp += mat[num]



N = int(input())
M = int(input())
mat = {}

for i in range(M):
    s , g = map(int,input().split())
    if mat.get(s) is None:
        mat[s]=[g]
    else:
        mat[s].append(g)

    if mat.get(g) is None:
        mat[g]=[s]
    else:
        mat[g].append(s)



# print(mat)

visited = []
dfs(1)
print(len(visited)-1)