def iswall(x,y):
    if x>0 and y>0 and x < N-1 and y <N-1:
        return False
    return True


def cal(t):
    while t>0: ## 시간진행
        for i in range(N):
            for j in range(N):
                if mat[i][j] !=0:
                    loc = mat[i][j]
                    if loc[1] ==1:

                    elif loc[1] ==2:

                    elif loc[1] ==3:

                    else:  #4인 경우





        t-=1



    pass

T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    datas = []
    mat = [ [0]*N for i in range(N) ]
    for i in range(K):
        x,y,n,dr = map(int,input().split())
        mat[x][y] =[n,dr]

    cal(M)