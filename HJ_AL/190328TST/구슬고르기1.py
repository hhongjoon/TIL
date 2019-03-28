def comb(n,k):
    if n == k:
        for i in range(3):
            if chk[i] == 1:
                print(i+1, end=" ")
            else:
                print(0, end=" ")
        print()
        return
    else:
        chk[k]=1
        comb(n,k+1)
        chk[k]=0
        comb(n,k+1)

chk= [0]*3
comb(3,0)