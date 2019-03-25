import sys
sys.stdin = open("노드의 합.txt")

def sum_leaf(N,L):
    for i in range(N,0,-1):
        if i == L:
            return tree[i]

        if i//2 >0:
            tree[i//2] += tree[i]



T = int(input())
for _ in range(T):
    N, M, L = map(int,input().split())
    tree = [0]*(N+1)
    for i in range(M):
        key, val = map(int,input().split())
        tree[key]=val
    print("#{} {}".format(_+1,sum_leaf(N,L)))
