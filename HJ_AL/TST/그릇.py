
input_data = list(input())

sum = 0
for i in range(len(input_data)):
    if i == 0:
        sum += 10
        continue
    if input_data[i] == '(':
        if input_data[i-1] == ')':
            sum += 10
        else:
            sum +=5

    else:
        if input_data[i-1] == ')':
            sum += 5
        else:
            sum +=10

print(sum)