def main():
    T = int(input())
    nums = list(map(int,input().split()))
    # print(nums)
    order=[]
    count = 0
    while len(nums) != 0:  ## 입력받은 숫자가 없을 때 까지
        num = nums[0]
        del nums[0]
        count +=1

        if num == 0:                ## 0 이면 이어서 추가
            order.append(count)
            # print(order)

        else:                       ## 자리값 계산해서 넣음
            temp_list = order[::]     ## 리스트 참조로 인한 복사본 만듬
            order[len(order) - num] = count         ## 먼저 앞자리에 숫자 넣음
            order = order[0:len(order) - num +1] + temp_list[len(order) - num:]  ## 슬라이싱 계산으로 이어서 연결
            # print(order)
    for i in range(T):
        print(order[i],end=" ")




if __name__=="__main__":
    main()