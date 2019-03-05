def cal_score(round):
    count = {}
    for i in range(ea):
        if count.get(round[i]) is None:
            count[round[i]] =[i]
        else:
            count[round[i]].append(i)
    for key,val in count.items():
        if len(val)==1:
            people[val[0]]+=key

ea = int(input())
round1=[]
round2=[]
round3=[]
people=[0]*ea
for i in range(ea):
    r1, r2, r3 = map(int,input().split())
    round1.append(r1)
    round2.append(r2)
    round3.append(r3)

cal_score(round1)
cal_score(round2)
cal_score(round3)

for i in people:
    print(i)
