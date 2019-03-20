ch16 = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}


def putnum(L):
    global l
    for i in range(4):
        if L[i * l:i * l + l] in result:
            continue
        result.append(L[i * l:i * l + l])
def cal(result,l):
    result2=[]
    for i in range(len(result)):
        piv = l-1
        val=0
        while piv>-1:
            num = result[i][piv]
            if num.isdigit():
                val += (16**(l-1-piv))*int(num)
            else:
                val += (16**(l-1-piv))*ch16[num]

            piv-=1
        result2.append(val)
    return result2

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    nums=list(input())

    l = N//4
    result = []
    # 0회전
    print(nums)
    putnum(nums)
    for i in range(l-1):
        # 1회전
        nums.insert(0,nums.pop())
        print(nums)
        putnum(nums)

    print(result)
    rr = cal(result,l)
    rr.sort(reverse=True)
    print(rr,len(rr))
    print("#{} {}".format(_+1,rr[K-1]))


