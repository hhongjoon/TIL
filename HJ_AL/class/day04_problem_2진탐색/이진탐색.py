import sys
sys.stdin = open("이진탐색_input.txt")
def binarysearch(a, key):
    count = 0
    start = 1
    end = a
    while start <= end:
        count += 1
        middle = int((end+start)/2)
        if key == middle:
            return count
        elif key < middle :
            end = middle
        else:
            start = middle

    return -1 ## 검색실패시


casecount = int(input())
for i in range(casecount):
    page, a, b = map(int, input().split())
    A = binarysearch(page, a)
    B = binarysearch(page, b)
    if A < B:
        print(f'#{i+1} A')
    elif A > B :
        print(f'#{i+1} B')
    else :
        print(f'#{i+1} 0')