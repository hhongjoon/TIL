num = 123123
c = [0]*12   # dummy로 만들어놓은 것, 오류 안뜨도록
for i in range(6):
    c[num%10] += 1
    num //=  10  # num = num//10

print(c)
i = 0
tri = 0
run = 0
while(i<10):
    if c[i] >= 3:
        c[i] -= 3
        tri == 1
        continue
    if c[i]>= 1 and c[i+1]>= 1 and c[i+2]>= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run +=1
        continue

    i += 1

if tri + run == 2:
    print("baby-jin")
else:
    print('not')
