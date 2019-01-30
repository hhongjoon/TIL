def binarysearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (end+start)//2
        if key == a[middle]:
            return middle
        elif key < a[middle] :
            end = middle -1
        else:
            start = middle + 1
    return -1 ## 검색실패시

key = 22
data = [12,22,24,36,52,56,72,91]
print(binarysearch(data, key))