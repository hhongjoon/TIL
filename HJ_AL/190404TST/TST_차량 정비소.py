T = int(input())
N, M, K, A, B = map(int,input().split())
A -= 1
B -= 1
reps = list(map(int,input().split())) # 접수
mecas = list(map(int,input().split())) # 정비
cus = list(map(int,input().split())) # 고객 도착시간
