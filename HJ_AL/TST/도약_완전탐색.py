T = int(input())
leaf = []
for i in range(T):
    leaf.append(int(input()))
leaf.sort()
# print(leaf)
sum = 0
for i in range(len(leaf) - 2):
    for j in range(i + 1, len(leaf) - 1):
        for k in range(j+1,len(leaf)):
            step1 = leaf[j] - leaf[i]
            step2 = leaf[k] - leaf[j]

            if step1<=step2 and step1*2 >= step2:
                sum+=1


print(sum)