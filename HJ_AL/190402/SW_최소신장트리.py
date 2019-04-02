T = int(input())
V, E = map(int,input().split())

datas = [ [0]*(V+1)  for i in range(V+1)  ]
for i in range(E):
    n1, n2, w = map(int,input().split())
    datas[n1][n2] = w
