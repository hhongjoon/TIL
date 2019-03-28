N = int(input())
datas = list(map(int,input().split()))
total = int(input())
datas.sort(reverse=True)
piv = sum(datas)//len(datas)
while True:
    piv = datas.pop()
    total = total - piv
    if len(datas) ==0 and total>=piv:
        result=piv
        break


    if total//len(datas) >= datas[-1]:
        continue
    else:
        result = total//len(datas)
        break
print(result)