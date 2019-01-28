

num = int(input())
count=0
for i in range(1,num+1):
    if len(str(i)) == 1 or len(str(i))==2:
        count += 1
        continue
    str_num=str(i)
    judge = True
    for j in range(0,len(str_num)-2):
        if int(str_num[j]) - int(str_num[j+1]) == int(str_num[j+1]) - int(str_num[j+2]):
            continue
        else:
            judge = False
            break
    if judge == True:
        count+=1
print(count)