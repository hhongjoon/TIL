import sys
sys.stdin = open("inorder.txt")

def inorder(root=1):
    temp = root
    if len(path[temp]) == 0:
        return True

    inorder(path[temp][0])
    print(chr[temp])
    inorder(path[temp][1])





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
    inorder(1)


