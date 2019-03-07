def main():
    T = int(input())
    values = []
    for i in range(T):
        values.append(float(input()))

    result = 1
    prev_list = []
    for i in values:
        prev = result
        result *= i
        if result < 1:
            prev_list.append(prev)
            result = 1
            continue
        if prev > result:
            prev_list.append(prev)


    print(round(max(prev_list),3))



def main2():
    T = int(input())
    values = []
    for i in range(T):
        values.append(float(input()))


    maxval = 0

    for i in range(T):
        val = 1
        for j in range(i,T):
            val *= values[j]
            if maxval <= val:
                maxval = val
    print('%.3f' % maxval)

def main3():
    T = int(input())
    values = []
    for i in range(T):
        values.append(float(input()))

    maxval = 0
    base = 1
    for i in range(T):
        base *= values[i]  # 곱해보고
        if base < values[i]:   #곱한것이 자기값보다 작으면, 값 대체
            base = values[i]
        if base > maxval:     # 최대값인지 확인
            maxval = base
    print('%.3f' % maxval)






if __name__ == "__main__":
    main3()