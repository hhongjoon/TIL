data = [int(input()) for i in range(3)]
#print(data)
mul_data = data[0]*data[1]*data[2]
result = [0]*10
for i in str(mul_data):
    result[int(i)] += 1
#print(result)

[print(u) for u in result]