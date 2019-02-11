
def insert(value):
    if len(result) == 0:
        result.append(value)
        #print(result)
        return result

    result.append(value)
    pivot = len(result)
    while True:
        prev = pivot
        pivot = int(pivot / 2)

        if pivot>0 and result[pivot-1] > value:
            result[pivot-1], result[prev-1] = result[prev-1], result[pivot-1]
            continue
        else:
            break
    #print(result)
    return result

def sum_heap(result):
    pivot = len(result)
    sum = 0
    while True:
        pivot = int(pivot/2)
        if pivot>0:
            sum += result[pivot - 1]
        else:
            return sum


T = int(input())
for _ in range(T):
    result = []
    ea = int(input())
    numbers = list(map(int,input().split()))
    for i in numbers:
        insert(i)

    print(result)
    print(f"#{_+1} {sum_heap(result)}")
