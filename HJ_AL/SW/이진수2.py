T = int(input())
for _ in range(T):
    num = float(input())
    cnt = 0
    base = 0.5
    result=""
    while True:
        if cnt>12 or num==0:
            break
        cnt+=1
        if num >= base:
            num -= base
            result += '1'
        else:
            result += '0'
        base /= 2

    print('#{} '.format(_+1), end="")
    if cnt>12:
        print('overflow')
    else:
        print(result)