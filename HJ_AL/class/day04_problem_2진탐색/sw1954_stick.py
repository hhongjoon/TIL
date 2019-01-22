import sys
sys.stdin = open("스틱_input.txt")

T = int(input())
for _ in range(T):
    ea = int(input())
    stick = list(map(int,input().split()))

    new_stick = []
    for ii in range(len(stick) -1 ):
        if ii%2 == 1:
            continue
        new_stick.append([stick[ii], stick[ii+1]])

    result = []
    result.append(new_stick[0])
    for i in range(len(new_stick)-1):

        for j in range(1,len(new_stick)):

            if result[-1][1] == new_stick[j][0]:
                result.append(new_stick[j])
                continue
            if result[0][0] == new_stick[j][1]:
                result.insert(0,new_stick[j])
                continue

    print(f'#{_+1}', end = " ")
    for k in range(len(result)):
        for kk in range(2):
            print(result[k][kk], end =" ")
    print()



