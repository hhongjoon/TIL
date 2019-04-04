
def dfs(n,k,cnt,prev):
    global mindis
    if cnt>mindis:
        return
    if n == k:
        if mat[prev][0] == 0:
            return
        mindis = min(mindis, cnt+mat[prev][0])
        return
    else:
        for i in range(N):
            if mat[prev][i] != 0 and visited[i] == False:
                visited[i]=True
                dfs(n,k+1,cnt+mat[prev][i],i)
                visited[i]=False

N = int(input())
mat = [ list(map(int,input().split())) for i in range(N) ]
visited=[False]*N
visited[0]=True
mindis = 0xffffff
dfs(N-1,0,0,0)
print(mindis)