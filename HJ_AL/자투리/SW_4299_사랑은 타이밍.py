T = int(input())
flag = True
for _ in range(1,T+1):
    D, H, M = map(int,input().split())
    if D <11:
        flag = False

    if D == 11 and H<11:
        flag = False

    if D == 11 and H == 11 and M<11:
        flag = False

    if flag:
        w_d = D-11
        w_h = H-11
        w_m = M-11
        # print(w_d, w_h, w_m)

        result = w_d*1440 + w_h*60 + w_m
        print("#{} {}".format(_,result))
    else:
        print("#{} {}".format(_,-1))