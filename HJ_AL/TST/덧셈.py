def make_num(nums_list):
    numlen = len(nums_list)
    result = 0

    while numlen>=1:    # 처음값 : 디폴트 0 이기 때문에 곱하기 해도 10 / 이후 값 부턴는 곱한이후에 deque하고 다음값 더해줌
        result *= 10
        result += nums_list[0]
        del nums_list[0]
        numlen -= 1
    # print(result)
    return result

def main():
    #입력부
    given, ans = map(int,input().split())   
    given_list = list(map(int,str(given)))
    # print(given_list)

    for i in range(1,len(given_list)):
        num1 = make_num(given_list[:i]) # for문을 통해 슬라이싱해서 함수 들어감
        num2 = make_num(given_list[i:])
        if num1 + num2 == ans:
            print("{0}+{1}={2}".format(num1,num2,ans))
            return
    print('NONE')


if __name__=="__main__":
    main()