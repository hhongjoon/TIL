import sys
sys.stdin = open("flatten_input.txt")

for i in range(10):
    count = int(input())
    dummy = list(map(int,input().split()))
    for a in range(count):
        maxdum, mindum =  -1, 9999999
        for dum in range(len(dummy)):
            if dummy[dum] > maxdum:
                maxdum, maxloc = dummy[dum], dum
            if dummy[dum] < mindum:
                mindum, minloc = dummy[dum], dum
        dummy[maxloc] -= 1
        dummy[minloc] += 1
    maxx = -1
    minn = 999999
    for ii in dummy:
        if ii > maxx :
            maxx = ii
        if ii < minn:
            minn = ii
    print(f"#{i+1} {maxx - minn}")