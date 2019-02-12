import sys
sys.stdin = open("inorder.txt")

def inorder(root=1):
    temp = root
    #print(temp, 'in')
    if len(path[temp]) == 0:  # 자식이 없다면, 탐색중 더 이상 가지못하므로 Print
        print(chr[temp], end="")
        return True

    inorder(path[temp][0])
    print(chr[temp], end="")

    if len(path[temp]) > 1 : #있을 때만
        inorder(path[temp][1])
    #return True





for _ in range(10):

    path = dict()
    chr = ['-']
    ea = int(input())
    for i in range(ea):
        data=[]
        data = list(map(str,input().split()))

        chr.append(data[1])
        if len(data) == 4:

            path[int(data[0])] = [int(data[2]), int(data[3])]

            continue
        if len(data) == 3:
            path[int(data[0])] = [int(data[2])]
            continue
        path[int(data[0])] = []
    #print(path)
    print(f'#{_+1}', end = " ")
    inorder(1)
    print()


