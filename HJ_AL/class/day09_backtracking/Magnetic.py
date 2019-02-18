import sys
sys.stdin = open("magnetic.txt")


def solve():
    count = 0
    for y in range(size):
        prev = 2
        for x in range(size):

            if mat[x][y] == 0:
                continue

            elif mat[x][y] == 2:
                if prev == 2:
                    continue

                if prev == 1:
                    count +=1
                    prev = 2 ## 초기화

            else:  # 1일때
                prev = 1
                continue

    return count






for _ in range(10):
    size = int(input())
    mat = [  [0 for i in range(100) ]  for i in range(100)   ]
    for i in range(100):
        mat[i] = list(map(int,input().split()))
    print(f"#{_+1} {solve()}")
