#  음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
#  예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오.
#  0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

dp={}
prob = int(input())  ## 몇번째 값을 구하는지
count = 10
result = 10
if prob <= 10:
    print(prob)
else:
    while(prob != result):
        count+=1
        numtostr = str(count)
        judge=True
        #print(dp)
        print(result, count)
        if dp.get(tuple(numtostr[0:len(numtostr)-1])) == None:  ## 리스트는 키로 쓸 수 없음
            for i in range(0, len(numtostr) - 1):  # 여기를 줄여야함
                if int(numtostr[i]) > int(numtostr[i + 1]):
                    continue
                else:
                    judge = False
                    break

            if judge == True:
                dp[tuple(numtostr)] = True
                result += 1
                continue



        elif dp[tuple(numtostr[0:len(numtostr)-1])] == True:          ##이전 값까지가 트루일 때
            if int(numtostr[-2]) > int(numtostr[-1]):
                dp[tuple(numtostr)] = True
                result+=1

            else:
                dp[tuple(numtostr)] = False

            continue # 다음




    print(count)
