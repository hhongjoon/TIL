
def perm(n,k, cnt):
    global mindis
    if mindis<cnt:
        return
    if n == k:

        mindis = min(mindis,cnt)
        return
    else:
        for i in range(k,N):
            robots[k] ,robots[i] = robots[i], robots[k]
            plus = abs(robots[k][0] - snacks[k][0]) + abs(robots[k][1] - snacks[k][1])
            perm(n,k+1,cnt+plus)
            robots[k], robots[i] = robots[i], robots[k]
T = int(input())
for _ in range(T):
    N = int(input())
    r = list(map(int,input().split()))
    s = list(map(int,input().split()))
    robots = []
    snacks = []
    for i in range(0,N*2,2):
        robots.append((r[i],r[i+1]))
        snacks.append((s[i],s[i+1]))
    mindis = 0xffffff
    perm(N,0,0)
    print(mindis)