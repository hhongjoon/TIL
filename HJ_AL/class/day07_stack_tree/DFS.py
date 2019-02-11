ea = int(input())


paths = list(map(int,input().split()))
paths2 =[]
for i in range(len(paths)):
    if i%2==0:
        paths2.append((paths[i],paths[i+1]))
print(paths2)
mat = [ [0 for j in range(8)]  for i in range(ea)]
print(mat)
for i in paths2:
    mat[i[0]][i[1]] = 1
    mat[i[1]][i[0]] = 1
for i in range(len(mat)):
    print(mat[i])

## 재귀 부분
root = 1
visited = [0 for i in range(ea)]   # 참조변수라서 재귀에서 접근가능

def dfs_recursive(v):
    if visited[v] == 0:
        visited[v] = 1
        print(v)

    for i in range(len(mat[v])):
        if mat[v][i] == 1:
            # print('i' , i)
            if visited[i] == 1:
                continue
            dfs_recursive(i)

dfs_recursive(root)





# for문사용 DFS

# root = 1
# temp = []
# temp.append(root)
# visited=[]
#
# while len(temp) > 0:
#     if temp[-1] not in visited:
#
#         next = temp.pop()
#         print(next)
#         visited.append(next)
#         for i in range(len(mat[next])):
#             if mat[next][i] == 1:
#                 temp.append(i)
#     else:
#         temp.pop()
#
# print(visited)




