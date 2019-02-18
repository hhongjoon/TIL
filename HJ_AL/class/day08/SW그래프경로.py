import sys
sys.stdin = open("그래프경로.txt")


def solve1(start, end, mat):
    if start == end:
        global ko  # 따로선언할 것
        ko = True
        return True

    for i in range(len(mat)):
        if mat[start][i] == 1:
            solve1(i, end, mat)

T = int(input())

for _ in range(T):
    V, E = map(int,input().split())
    mat = [ [0 for j in range(V+1)] for i in range(V+1) ]
    for i in range(E):
        a, b = map(int,input().split())
        mat[a][b] = 1


    start, end = map(int,input().split())
    ko = False

    solve1(start, end,mat)
    print(f"#{_ + 1} {int(ko)}")








# def solve(start,end,mat):
#
#     for i in range(len(mat[start])):# 처음 시작값에서 for문/끝난다면 return 0
#
#         if mat[start][i] == 0: #
#             continue
#
#         count = 0
#         rotate = i
#         while count <len(mat):  # 노드의 갯수만큼 돌린다.  # 찾았을 때
#
#             if mat[rotate][count] == 0:  # 없으면 증가시키고 다음 검색
#                 count+=1
#                 continue
#
#             else :
#                 print(i)
#                 rotate = count
#                 count = 0
#                 if rotate == end:
#                     #print(end)
#                     return 1
#
#     return 0