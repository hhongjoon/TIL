def depth_fs(graph , root):   ## 그래프는 딕셔너리에 value값을 set로 구조 설정
    visited = []
    temp = []
    temp.append(root)
    while len(temp) > 0:   # 끝에서부터 돌아간다.
        root = temp.pop()
        if root not in visited:
            temp = temp + list(graph[root])
            visited.append(root)
    return visited

def breath_fs(dict_a, root):
    visited = []
    visited.append(root)  # 첫방문 넣어줌
    Q = []
    Q.append(root)   # 임시 저장소, 다음 수행해야할 것들
    while len(Q) != 0:

        for neighbor in dict_a[Q.pop(0)]:      # set 요소들이 차례로 들어가서 visted에 없으면 추가, 없으면 넘어감,
            if neighbor not in visited:        #  차례로 쌓이고 Q 가 없어질때까지 반복
                visited.append(neighbor)
                Q.append(neighbor)

    return visited

def main():
    m, n, root = map(int,input().split())
    graph = {}
    for i in range(n):
        p, q = map(int, input().split())
        if p in graph:
            graph[p].append(q)
            if q not in graph:
                graph.setdefault(q, [])
        else:
            graph.setdefault(p, [q])
            if q not in graph:
                graph.setdefault(q, [])
    for i in graph:
        graph[i].sort()
    #print(graph)
    #bfs 적용
    result_bfs = breath_fs(graph,root)
    for i in graph:
        graph[i].sort(reverse = True)
    #print(graph)
    print(depth_fs(graph,root))
    print(result_bfs)


if __name__ == "__main__":
    main()


# 7 8 0
# 0 1
# 0 5
# 0 4
# 1 6
# 1 2
# 2 3
# 3 0
# 5 2