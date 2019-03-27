


def cal(num,datas):
    loc = 0
    while True:
        if len(datas) ==0:
            return 0

        else:
            dis = len(datas)
            piv = datas[dis//2]
            if num>piv:
                datas=datas[(dis//2)+1:]
                loc+=dis//2+1
            elif num == piv:
                loc += dis//2 + 1
                return loc

            else:
                datas = datas[:dis//2]




N = int(input())
datas = list(map(int,input().split()))
goal = int(input())
datas_g = list(map(int,input().split()))

for i in datas_g:
    print(cal(i,datas))




