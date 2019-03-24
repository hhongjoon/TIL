def cal(num2,num3,n2_10,n3_10):
    n = len(num2)-1
    for i in range(n,0,-1):
        temp = n2_10
        if num2[i] == '0':
            temp += 2**(n-i)
        else:
            temp -= 2 ** (n - i)

        for j in range(len(num3)-1,-1,-1):

            val = int(num3[j])
            for k in range(3):
                t3=num3[:]
                if val == k:
                    continue
                t3[j] = str(k)
                t3_10 = int("".join(t3),3)
                if temp == t3_10:
                    return temp


T = int(input())
for _ in range(T):
    num2 = list(map(str,input()))
    n2_10 = int("".join(num2),2)
    # print(num2_10)
    num3 = list(map(str, input()))
    n3_10 = int("".join(num3),3)
    # print(num2_10)
    # print(num3_10)
    print("#{} {}".format(_+1,cal(num2,num3,n2_10,n3_10)))






