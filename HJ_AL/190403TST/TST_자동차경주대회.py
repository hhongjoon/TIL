
def findidx(prev,now):
    temp=[]
    for i in range(len(datas)):
        if prev < datas[i] and datas[i] <=now:
            temp.append(i)
    return temp

def cal(st,goal,prev,now,time):
    # print(now)
    global mintime
    if mintime < time:
        return

    if now>=goal:
        if mintime>time:
            mintime = time
        return
    idxs = findidx(prev, now)
    for i in idxs:
        # print(i)
        cal(st,goal,datas[i],datas[i]+D,time +times[i])


D = int(input())
N = int(input())
data_in = list(  map(int,input().split())  )
datas=[0]
for i in range(len(data_in)):
    datas.append(datas[i]+data_in[i])
print(datas)


times = list( map(int,input().split()) )
times.insert(0,0)

mintime = 0xffffff
cal(0,sum(data_in),0,D,0)
print(mintime)