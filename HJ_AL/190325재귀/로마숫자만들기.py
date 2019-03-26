def roma(n,rem,res,card):
    if rem == 0:
        if res not in result:
            result.append(res)
        return

    if card == 4:
        return

    else:
        for i in range(rem+1):
            plus = (datas[card]) * i
            roma(n,rem-i,res+plus,card+1)

result = []
datas = [1,5,10,50]
N = int(input())
roma(N,N,0,0)
print(len(result))