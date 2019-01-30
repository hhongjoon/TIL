m, n = map(int, input().split())
aa = list(range(1,m+1))
result = []
pivot = 0
while len(aa)>0:
    #print(pivot)
    if pivot + (n-1) >= len(aa):
        pivot = (pivot + n-1)%len(aa)            ## 나머지로 접그하자!!
    else:
        pivot = pivot+(n-1)
    result.append(aa[pivot])
    del aa[pivot]
    #print(aa,end = "    ")
    #print(result)
#print(result)

pp = '<'
for i in result:
    pp = pp + str(i)
    if i != result[-1]:
        pp = pp+', '
print(pp+'>')