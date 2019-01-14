def bread_fs(dict_a, root):
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
    graph = { 0:set([1,4,5]),
              1:set([2,6]),
              2:set([3]),
              3:set([0]),
              4:set([1]),
              5:set([2]),
              6:set()
    }

    print(bread_fs(graph, 0))


if __name__ == "__main__":
    main()