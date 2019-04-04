mat = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15,
    }


def makedec(L):
    tt = len(temp) -1
    summ = 0
    for i in range(len(temp)):
        if temp[i].isalpha():
            summ += mat[temp[i]]*(16**(tt-i))
        else:
            summ += int(temp[i])*(16**(tt-i))

    return summ
N, K = map(int,input().split())
datas = list(map(str,input()))

n = N//4 # 회전수
datas = datas[:] + datas[:n-1]

result = set()
for _ in range(n): # 회전 수
    for j in range(4):
        temp = datas[_+j*n:_+(j+1)*n]
        res = makedec(temp)
        result.add(res)
result = list(result)
result.sort(reverse=True)
print(result[K-1])
