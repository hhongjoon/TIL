import sys
sys.stdin = open("GNS_input.txt")
def GNS(data):
    for i in data:
        counting[i] += 1
    for ii, jj in counting.items():
        for _ in range(jj):
            print(ii, end=" ")
    print()

T = int(input())
for tc in range(T):
    temp = input()
    data = list(map(str,input().split()))
    counting = {
        "ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0,
        "SVN" : 0, "EGT" : 0, "NIN" : 0
                }
    print(f"#{tc+1}")
    GNS(data)