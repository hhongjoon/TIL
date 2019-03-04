import sys
sys.stdin = open("노드의 거리.txt")

def find_result(start, goal, temp):
    temp.append(start)
    while len(temp) != 0:

        tempval = temp.pop(0)
        if visited[start] == 0:
            visited[tempval] += 1

        for i in mat[tempval]:
            if visited[i] == 0:
                visited[i] = visited[tempval] + 1
                temp = temp + mat[tempval]


        visited[0] += 1
        if visited[goal] != 0:
            return visited[goal]-1

    return 0


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
    #print(mat)
    start, goal = map(int,input().split())

    visited=[0]*(V+1)
    temp = []
    final_len = find_result(start, goal, temp)
    print("#{0} {1}".format(_+1,final_len))