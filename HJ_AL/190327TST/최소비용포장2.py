N = int(input())
datas = list(map(int,input().split()))
total = 0
datas.sort()
while len(datas) >0:
    dis=datas[0]+datas[1]
    total+=dis
    datas.append(dis)
    datas=datas[2:]
    datas.sort()
    if len(datas) == 1:
        break
print(total)

