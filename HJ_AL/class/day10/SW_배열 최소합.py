import sys
sys.stdin = open("배열최소합.txt")

def backtrack(level, goal ,sum, check):
    global min_sum
    if sum > min_sum:
        return
    if level == goal: # 도착

        if min_sum > sum:
            min_sum = sum

    else :
        level +=1

        for i in range(goal):
            if check[i] == False:
                check[i]=True

                backtrack(level,goal,sum+mat[level-1][i], check)
                check[i]=False  # 돌아갈때 false 해주어야 다음에 진행 가능


T = int(input())
for _ in range(T):
    size = int(input())
    mat = [ list(map(int,input().split())) for i in range(size)     ]
    #print(mat)
    min_sum=99999999
    sum = 0
    check = [ False]*size
    backtrack(0,size,sum, check)
    print(f"#{_+1} {min_sum}")