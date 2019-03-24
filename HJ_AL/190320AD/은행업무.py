

T = int(input())
for _ in range(T):
    num2 = list(map(str,input()))
    num2_10 = int("".join(num2),2)
    # print(num2_10)
    num3 = list(map(str, input()))
    num3_10 = int("".join(num3),3)
    # print(num2_10)
    # print(num3_10)

    if num3_10 >= num2_10:
        distance = num3_10 - num2_10
        piv = 3
    else:
        distance = num2_10 - num3_10
        piv = -3

    # print(distance)

    if piv==3: # 3진수가 더클 때, 2진수를 더해야함
        n=0
        while distance - 2**n>0:
            n+=1
        n = n-1  # 자리값
        while num2[len(num2) - 1 - n] == '1':
            n-=1
        num2[len(num2) - 1 - n] = str(int(num2[len(num2)-1 -n]) + 1)
        print("#{} {}".format(_ + 1, int("".join(num2), 2)))

    else:  # 2진수가 더클때
        n = 0
        while distance - 2**n>0:
            n+=1
        n= n-1
        if n==len(num2)-1:
            n-=1
        while num2[len(num2) - 1 - n] == '0':
            n-=1

        num2[len(num2)-1 -n] = str(int(num2[len(num2)-1 -n]) - 1)
        print("#{} {}".format(_+1,int("".join(num2), 2)))