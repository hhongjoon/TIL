
def findmin():
    mindis = 999999
    minidx = 0
    for i in range(N+1):
        if visited[i] == 0 and W[i] < mindis:
            minidx = i
            mindis = W[i]
    return minidx  # 방문 안한 것들 중 최소 값의 인덱스


def dijkstra(goal):
    W[0] = 0
    for i in range(N+1):
        if datas[0][i] != 0:
            W[i] = datas[0][i]
    visited[0] = 1 # 방문함 (첫번째)

    while True:
        node = findmin()
        visited[node] = 1
        if node == goal:
            return W[node]

        for i in range(N+1):
            if datas[node][i]:
                if W[i] > W[node] + datas[node][i]:
                    W[i] = W[node] + datas[node][i]





T = int(input())
for _ in range(1,T+1):
    N, E = map(int,input().split())
    datas = [ [0]*(N+1) for i in range(N+1) ]
    visited = [0]*(N+1)
    W = [99999999]*(N+1)

    for i in range(E):
        st, go, w = map(int,input().split())
        datas[st][go] = w

    res = dijkstra(N)
    print('#{} {}'.format(_, res))