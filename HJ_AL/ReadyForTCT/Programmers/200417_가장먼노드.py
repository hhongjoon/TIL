# 자료형 딕셔너리 양방향으로 mapp = {0:[1,2,3], 1:[2,4]}


def solution(n, edge):
    def bfs():
        visited[1] = 0
        temp = [(1,0)]
        while True:
            if len(temp) == 0:
                return visited
            val = temp.pop(0)
            for i in mapp[val[0]]:
                if visited[i] == -1 or visited[i]>val[1]+1:
                    visited[i] = val[1]+1
                    temp.append((i,val[1]+1))
                else:
                    continue

        return visited

    mapp = {}
    for i in range(1,n+1):
        mapp[i] = list()
    for i, j in edge:
        mapp[i].append(j)
        mapp[j].append(i)

    #print(mapp)

    visited = [-1]*(n+1)
    result = bfs()
    #print(result)
    aa = max(result)
    answer = result.count(aa)

    return answer


print(solution(100,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))