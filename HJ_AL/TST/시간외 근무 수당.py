def main():                 ## 자료형 주의할 것
    hours = 0
    for i in range(5):   # 데일리 초과된 시간 계산해서 일주일치 더함
        start, end = map(float,input().split())
        if end - start <= 1:
            continue
        else:
            daily = end - start -1
            if daily > 4:
                hours += 4
            else:
                hours += daily


    
    if hours >= 15:            ## 조건별로 돈 계산
        money = hours*10000*0.95

    elif hours <=5 :
        money = hours*10000*1.05

    else:
        money = hours * 10000

    print(int(money))


if __name__ == "__main__":
    main()