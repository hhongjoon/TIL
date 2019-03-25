pat=[
    '0001101',
    '0011001',
    '0010011',
    '0111101',
    '0100011',
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011'
]


pat16={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',

}
def getpat(codes,rate):

    pass



def findpat(codes):
    rate=[]
    ratecnt=0
    piv=0
    for i in range(len(codes)-1,-1,-1):
        if codes[i]=='1':
            if st not in locals():
                st = i
            if len(rate)!=0 and piv==0:
                rate.append(ratecnt)
                ratecnt=0

            ratecnt+=1
            piv=1
        else:
            if len(rate)==0 and ratecnt==0:
                continue
            if piv==1 and len(rate)==2:
                rate.append(ratecnt)
                return rate, st

            if piv == 1:
                rate.append(ratecnt)
                ratecnt=0
            ratecnt+=1
            piv=0






T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    mat = [ list(input()) for i in range(N)]

    newmat=[]


    for i in range(N):
        zerocheck = True
        temp=''
        for j in range(M):
            temp += pat16[mat[i][j]]
            if '1' in pat16[mat[i][j]]:
                zerocheck = False
        if zerocheck:
            continue
        else:
            newmat.append(temp)

    checklen=[0,0,0]
    for i in range(len(newmat)):
        print(newmat[i])
        t = findpat(newmat[i])
        rate = min(t)


