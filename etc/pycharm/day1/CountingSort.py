def count(a,b,c):         ## 다시
    for i in range(len(b)):
        c[a[i]] += 1
    #print(c)
    for i in range(1, len(c)):
        c[i] += c[i-1]
    print(c)
    for i in range(len(b)-1,-1,-1):
        b[ c[a[i]]-1 ] = a[i]          ## 갯수라서 1부터 시작 따라서 -1 해줘야함
        c[a[i]] -= 1
        #print(b, 'b', i)
    return
a = [0,4,1,3,1,2,4,1]   ## 11개
b= [0]*len(a)
c= [0]*50     ## 해당 숫자자리를 찾아서 카운트 0도 포함
count(a,b,c)

print(b)