def bubble(data):   ## call by reference 확실히 알고 가자
    for i in range(len(data)-1,0,-1): #4 3 2 1
        for j in range(0,i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def bubble_reverse(data):
    for i in range(len(data)-1,0,-1):
        for j in range(0,i):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


data = [55, 7, 78, 12, 42]

bubble(data)
print(data)
bubble_reverse(data)
print(data)