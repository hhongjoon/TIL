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


def main():
    graph = { 0:set([1,4,5]),
              1:set([2,6]),
              2:set([3]),
              3:set([0]),
              4:set([1]),
              5:set([2 ,7]),
              6:set(),
              7:set([8,9]),
              8:set(),
              9:set([3])
    }

    print(depth_fs(graph, 0))
if __name__ == "__main__":
    main()