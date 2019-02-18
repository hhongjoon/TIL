import sys
sys.stdin = open("작업순서_input.txt")
def solve(mat, root):
    visited = []
    visited+= root
    temp = []
    temp += root

    while len(temp) != 0:

        for neighbor in mat[temp.pop(0)]:
            if neighbor not in visited and isok(neighbor,visited) :
                visited.append(neighbor)
                temp.append(neighbor)

    return visited

def isok(data, visited): ## 만족이 되는지
    ok = []
    for key, val in mat.items():
        if data in val:
            ok.append(key)
    if set(ok)&set(visited) == set(ok):
        return True
    return False


for _ in range(10):
    V, E = map(int,input().split())
    E_input = list(map(int,input().split()))
    mat = dict()

    for i in range(1,V+1):
        mat[i] = []

    for i in range(len(E_input)):
        if i%2 == 0:
            mat[E_input[i]].append(E_input[i+1])


    # for i in range(len(E_input)):
    #     if E_input[i] not in mat:
    #         mat[E_input[i]]=[]
    #     if i%2 == 0:
    #         mat[E_input[i]].append(E_input[i+1])

    #print(mat)
    root2 =[i for i in range(1,V+1)]
    #print(root2,'root2')
    root1 = []
    for i in mat.values():
        root1 += i
    root = set(root2) - set(root1)
    #print(set(root2) - set(root1))

    #print(root)
    result = solve(mat, list(root))
    print(f"#{_+1} ",end=" ")
    for i in result:
        print(i,end=" ")
    print()