import sys
sys.stdin = open("노드의 거리.txt")

def find_result(start, goal, distance):
    visited.append(start)
    print(start,goal, visited)
    # global flag
    # if flag:
    #     return
    if goal in mat[start]:

        global final_len
        # flag = True
        if distance + 1 < final_len:
            final_len = distance+1
        return

    for i in mat[start]:
        if i not in visited:
            find_result(i,goal,distance+1)




T = int(input())
for _ in range(T):
    V, E = map(int,input().split())
    mat = {}
    for i in range(1,V+1):
        mat[i]=[]
    for i in range(E):
        key, val = map(int, input().split())
        mat[key].append(val)
        mat[val].append(key)
    print(mat)
    start, goal = map(int,input().split())
    final_len = 9999999
    flag = False
    visited=[]
    find_result(start, goal, 0)
    print(f"#{_+1} {final_len}")