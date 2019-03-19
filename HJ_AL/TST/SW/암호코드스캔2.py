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

p16={
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









#
# def find16(codes):
#
#     flag = False
#     code02=''
#
#     for i in range(len(codes)):
#         if codes[i] != '0' or flag:
#             # print(codes[i])
#             flag = True
#             num =  codes[i]
#             if ord(num) > ord('9'):
#                 code02 += pattern16[ord(num)-ord('A')+10]
#
#             else:
#                 code02 += pattern16[ord(num)-ord('0')]
#
#         flist.append(temp)
#     return code02

def findpat(c):
    cnt=0
    rate=1
    result = []  # 일시적

    while True:
        flag=False
        while len(result)<8:
            for i in range(len(pattern)):           # 패턴찾는 코드 찾으면 +7 못찾으면 +1 다시
                flag = False
                if c[cnt:cnt+7*rate] == pattern[i]: # 맞는 패턴있는지 검사
                    print(result, cnt)
                    result.append(i)

                    flag = True
                    break
            if len(result) == 8:
                find = True
                break

            if flag == True:
                cnt = cnt + 7 * rate  # 찾으면 다음패턴 검사
                continue
            else:
                cnt +=1                            # 없다면 1씩증가

        if len(result) == 8 and result not in flist:
            print(result)
            cnt += 1
            flist.append(result)
            result=[]

        elif cnt == len(c):

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

    newmat=[]

    for i in range(N):
        temp=''
        for j in range(M):
            temp += p16[mat[i][j]]
        newmat.append(temp)
    print(newmat)

    for i in range(N):
        findpat(newmat[i])









    # codes = mat[x][0:y+1]
    # print(codes)
    #
    # c02 = find16(codes)
    # print(c02)
    # result = findpat(c02)
    # print(result)
    # fresult.append(result)
    #
    # #가로 검사
    # codes=[x][c02[1]]