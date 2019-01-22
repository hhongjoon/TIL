def selection(a):
    for i in range(0,len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                a[min], a[j] = a[j],a[min]

a = [64, 25, 10, 22, 11]
selection(a)
print(a)