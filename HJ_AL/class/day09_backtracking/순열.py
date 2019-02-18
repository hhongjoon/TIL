def process_solution(a,k):  ##  출력부
    for i in range(1,k+1):
        print(data[a[i]], end=" ")
    print()


def make_candidates(a,k,input,c):  ##자리값에 따라서 존재하면 True 나머지 부분에 대해서 후보자수(ncands)를 설정
    in_perm = [False]*NMAX

    for i in range(1,k):
        in_perm[a[i]] = True
    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands +=1

    return ncands


def backtrack(a, k, input):  # 실행부
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a,k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):

            a[k] = c[i]
            backtrack(a,k,input)




MAXCANDIDATES = 100  # 초기설정
NMAX = 100
data = [0,1,2,3,4,5]
a = [0]*NMAX
# total_cnt = 0
# cnt = 0
backtrack(a,0,5)
