# def findset(N):
#
#
# def kruskal(G,w)
#     A=[]
#
#     for i in range(len(datas)):
#         if findset(datas[i]) == True: # 순환이면 continue
#             continue
#         else:
#             A.append(datas[i])
#
#
# T = int(input())
# for _ in range(T):
#     V,E = map(int,input().split())
#     datas=[]
#     for i in range(E):
#         st, g, w = map(int,input().split())
#         datas.append((st,g,w))
#     datas.sort(key = lambda w:w[2])
#     print(datas)

def findSet(x):
    if x == p[x]: return x         # 대표 원소면 리턴
    else: return findSet(p[x])     # 대표 원소가 아니라면

def mst():
    global V
    c = 0  # 간선개수
    s = 0  # 가중치의 합
    i = 0  # 제어변수
    while c < V:                    # MST 구성을 위해 V개의 간선을
        p1 = findSet(edge[i][0])    # 두 노드의 대표 원소 알아내기
        p2 = findSet(edge[i][1])
        if p1 != p2:                # 사이클이 생성되지 않으면
            s += edge[i][2]         # MST에 포함되므로 가중치 추가
            c += 1                  # 간선 개수 증가
            p[p2] = p1              # 대표 원소 관리(union)
        i += 1                      # 저장된 다음 간선으로 이동
    return s                        # MST 완성 후 가중치 합 반환


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)] # 시작, 끝, 가중치
    edge.sort(key=lambda x : x[2])                             # 간선을 가중치 기준 오름차순으로 정렬
    p = list(range(V+1))                                       # 대표원소 초기화 (make set)
    print('#{} {}'.format(tc+1, mst()))