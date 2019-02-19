import sys
sys.stdin = open("card.txt")

def solve(people):
    #print(people)

    if len(people) == 1:
        return people[0]
    if len(people) == 2:
        return result_rpb(people[0] , people[1])

    L = solve(people[0:(len(people)-1)//2 + 1])
    R = solve(people[(len(people)-1)//2+1:len(people)])

    return solve([L,R])

def result_rpb(a,b):
    if a[1]>b[1]:  # b가 더 큰수
        a,b = b, a

    if a[1]==1 and b[1] == 2:
        return b
    if a[1]==2 and b[1] ==3 :
        return b
    if a[1]==1 and b[1] ==3:
        return a
    if a[0]<b[0]:
        return a
    else:
        return b


T = int(input())
for _ in range(T):
    size = int(input())

    RSP = list(map(int,input().split()))
    people = []
    for i in range(len(RSP)):
        people.append((i,RSP[i]))

    #print(people)
    print(f"#{_+1} {solve(people)[0]+1}")