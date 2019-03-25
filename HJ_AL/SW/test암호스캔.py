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
            return result
        else:
            rate+=1
            cnt=0
            result=[]
def find16(codes):

    flag = False
    code02='00000000000000000000000000000'
    for i in range(len(codes)):

        if codes[i] != '0' or flag:
            print(codes[i])

            flag = True
            num =  codes[i]
            if ord(num) > ord('9'):
                code02 += pattern16[ord(num)-ord('A')+10]

            else:
                code02 += pattern16[ord(num)-ord('0')]
    return code02
ex='000000110011110000001100111100000011001111000000110011110000001100111100000011001111000000110011110000001100111100000011001111'
findpat(ex)