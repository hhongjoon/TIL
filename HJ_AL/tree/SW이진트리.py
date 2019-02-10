#이진트리 root값 구하기

#case1 - 완전이진트리
#N = 2**n - 1 (n>=1)일때, root = int(N/2) + 1

#case2 오른쪽 비었을 때, 어떻게 비었는지 따질까?             => case 1,2 포함
#0<= 2**n - 1 - N < n           ,root = int(2**n-1/2) + 1

#case3 왼쪽 비었을 때,
# 2**(n-1)-n <= 2**n -1 - N<= 2**(n-1) - 1 일 때, root = int(2**n-1/2) - (n)

T = int(input())
for _ in range(T):
    N = int(input())
    #root구하기
    count =0
    while True:
        count +=1
        if N <=2**count - 1 and N > 2**(count-1) - 1:
            level = count
            break
    root = int((2 ** level - 1) / 2) + 1
    if N == 2**level-1:
        # root = int(N/2)+1  # pass
        pass
    elif (2**level - 1) - (2**(level-2)) <= N:
        # root = int((2**level - 1)/2) + 1  # pass
        pass
    else:
        root = root - ((2 ** level - 1) - (2 ** (level - 2)) -N)
    #print(root)

    # N/2 노드의 값
    result = N - (2 **(level - 1) - 1)        # 맨 밑층에서 몇번 째 인지
    val = 2 * result - 1
    if result % 2 == 0: #짝수번 일 때
        answer = val - 1
    else:               # 홀수번 일 때
        answer = val + 1
    print(f"#{_+1} {root} {answer}")





    # if (2**level - 1) - (2**(level-2)) < N :
    #    result = N - (2**(level-2) - 1 )
    #    val = 2*result -1
    #    if result % 2 ==0:
    #        answer = result - 1
    #    else:
    #        answer = result + 1
    #
    # else:
    #     result = N - (2 ** (level - 2) - 1)
    #     val = 2 * result - 1
    #     if result % 2 == 0:
    #         answer = result - 1
    #     else:
    #         answer = result + 1


