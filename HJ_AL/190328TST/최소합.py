def rec(n,v,cnt):  ## 모두 탐색
    global minval
    if minval<cnt:
        return

    if n == v:
        if minval>cnt:
            minval = cnt
        # print(cnt)
    else:
        for i in range(n):
            plus = mat[v][i]
            rec(n,v+1,cnt+plus)




def recdfs2(n,v,cnt): ## 열 중복 X
    global minval
    if minval<cnt:
        return

    if n == v:
        # print(cnt)
        if minval>cnt:
            minval = cnt
        # print(cnt)
    else:
        for i in range(n):
            if visited[i]==0:
                visited[i]=1
                plus = mat[v][i]
                recdfs2(n,v+1,cnt+plus)
                visited[i]=0


N = int(input())
mat = [ list(map(int,input().split())) for i in range(N) ]
# print(mat)


minval = 0xffffff
rec(N,0,0)            # 전부탐색/ 중복조합
print(minval)





visited=[0]*N
minval = 999999
recdfs2(N,0,0)
print(minval)

