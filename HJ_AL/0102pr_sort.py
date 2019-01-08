n = input()
n = str(n)

kk = list()
for i in n:
    kk.append(int(i))

kk.sort(reverse=True)
#print(kk)
for j in kk:
    print(j,end="")