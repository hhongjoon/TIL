def inorder(num,N):
    global idx
    if num<=N:
        inorder(num*2,N)
        tree[num]=idx
        idx+=1
        inorder(num*2+1,N)

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0]*(N+1)
    idx=1
    inorder(1,N)
    print("#{} {} {}".format(_+1,tree[1],tree[N//2]))
