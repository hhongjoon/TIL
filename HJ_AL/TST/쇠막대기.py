data = list(input())

sticks=[]
count = 0

for i in range(len(data)):
    bar = data[i]
    if bar == '(':
        sticks.append(bar)
    else:
        if data[i-1] == '(': # 레이져
            sticks.pop()
            count += len(sticks)
        else:               # 막대
            sticks.pop()
            count+=1

print(count)




