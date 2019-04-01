def cal(i):
    Q = []
    Q.append(i)
    while len(Q)>0:
        temp = Q.pop(0)





#======  main ==================
N, M = map(int,input().split())
mat={}
for i in range(1,N+1):
    mat[i]=[]
# print(mat)
for _ in range(M):
    st, goal = map(int,input().split())
    mat[goal].append(st)
# print(mat)
visited = [ [0]*N for i in range(N) ]
cal(i)

