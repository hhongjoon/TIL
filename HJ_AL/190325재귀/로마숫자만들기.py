def roma(n,rem,res,card):
    if card == 4:
        return
    if rem == 0:
        if res not in result:
            result.append(res)
        return
    else:
        for i in range(rem):
            plus = (datas[card]) * (n-i)
            roma(n,,res+plus,card+1)

    pass
result = []
datas = [1,5,10,50]
N = int(input())
roma(N,N,0,0)
print(len(result))