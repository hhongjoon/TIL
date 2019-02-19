def process_solution(a,k):  ##  출력부 k = 4 일 때 a[i] 를 인덱스로 넣어서 값 출력
    for i in range(1,k+1):
        print(data[a[i]], end=" ")
    print()


def make_candidates(a,k,input,c):  ##자리값에 따라서 존재하면 True 나머지 부분에 대해서 후보자수(ncands)를 설정
    in_perm = [False]*NMAX

    for i in range(1,k):# k 값에 따라서 어느 자리까지 채워졌는지 T/F 로 확인 , 채워졌으면  True
        in_perm[a[i]] = True    # 숫자가 사용되고 있으면 in_perm (인덱스)  True. a[i] 값을 훑어서 존재 값 확인
    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False: # in_perm 이 False 즉, 안쓰고 있는 숫자 발견하면 그 숫자를 'c'리스트에 저장 후 갯수 세어줌 backtracking으로 돌아갔을 때 갯수만큼 for문
                                    # 왜냐하면, 넣을 수 있는 숫자의 갯수라서 계속 재귀로 반복
            c[ncands] = i  # 후보자 가능 숫자? index가 c 리스트(후보가능 숫자)로 들어감. 앞에서부터 차곡차곡
            ncands +=1

    return ncands  # 후보자 갯수 반환


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
            backtrack(a,k,input)  # 재귀이기 때문에 들어가 버림




MAXCANDIDATES = 100  # 초기설정
NMAX = 100
data = [0,1,2,3,4]
a = [0]*NMAX
# total_cnt = 0
# cnt = 0
backtrack(a,0,4)
