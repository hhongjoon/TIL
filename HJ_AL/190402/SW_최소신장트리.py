
def findset(n): # 대표값으로 접근
    while p[n] != n:
        n = p[n]
    return n

def mst():
    global V
    c=0
    s=0

    i=0
    while c<V: # 노드의 수보다 1개 적은 간선 필요
        p1 = findset(edge[i][0])
        p2 = findset(edge[i][1])
        if p1 != p2:
            s+= edge[i][2]
            c+=1
            p[p2] = p1 # 대표값 설정
        i+=1
    return s


T = int(input())
for _ in range(T):
    V, E = map(int,input().split())
    edge = [list(map(int, input().split())) for i in range(E)]
    edge.sort(key=lambda x:x[2]) # 거리순으로 정렬
    p = list(range(V+1))
    res = mst()
    print('#{} {}'.format(_+1, res))

