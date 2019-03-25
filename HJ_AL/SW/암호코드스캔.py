pattern=[
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

pattern16=[
    '0000',
    '0001',
    '0010',
    '0011',
    '0100',
    '0101',
    '0110',
    '0111',
    '1000',
    '1001',
    '1010',
    '1011',
    '1100',
    '1101',
    '1110',
    '1111',

]

def find16(codes):

    flag = False
    code02='00000000000000000000000000000'
    temp=''
    for i in range(len(codes)):

        if codes[i] != '0' or flag:
            temp+=codes[i]
            # print(codes[i])


            flag = True
            num =  codes[i]
            if ord(num) > ord('9'):
                code02 += pattern16[ord(num)-ord('A')+10]

            else:
                code02 += pattern16[ord(num)-ord('0')]

        flist.append(temp)
    return code02

def findpat(c):
    cnt=0
    rate=1
    result = []
    while True:

        while len(result)<8:

            if len(c) < cnt:
                break
            for i in range(len(pattern)):           # 패턴찾는 코드 찾으면 +7 못찾으면 +1 다시
                flag = False
                if c[cnt:cnt+7*rate] == pattern[i]:
                    print(result, cnt)
                    result.append(i)
                    cnt = cnt + 7 * rate
                    flag = True
                    break
            if flag == True:
                continue
            else:
                cnt +=1

        if len(result) == 8:
            flist.append(result)
            result=[]
            cnt=0
            return
        else:
            rate+=1
            cnt=0
            result=[]




T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    mat = [ list(input()) for i in range(N)]
    # print(mat)
    fresult = []
    flist = []

    flag = False
    for i in range(len(mat)):
        for j in range(len(mat[0])-1,-1,-1):
            if mat[i][j] != '0':
                x,y = i,j
                flag = True
                break
        if flag == True:
            break
    codes = mat[x][0:y+1]
    print(codes)

    c02 = find16(codes)
    print(c02)
    result = findpat(c02)
    print(result)
    fresult.append(result)

    #가로 검사
    codes=[x][c02[1]]




















# num16 = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0],
#     [0, 0, 1, 1],
#     [0, 1, 0, 0],
#     [0, 1, 0, 1],
#     [0, 1, 1, 0],
#     [0, 1, 1, 1],
#     [1, 0, 0, 0],
#     [1, 0, 0, 1],
#     [1, 0, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0],
#     [1, 1, 1, 1],
#
# ]