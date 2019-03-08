def cal(dep):
    if len(data) == 0:
        return

    val = data.pop(0)
    if val != '<' and val != '>':
        while True:
            if data[0] != '<' and data[0] != '>':
                val += data.pop(0)
            else:
                break


    if val =='<':
        cal(dep+1)
        return cal(dep)
    elif val == '>':
        return
    else:
        if dep == level:
            print(val,end=" ")
        return cal(dep)





global level
level, data = map(str,input().split())
level = int(level)
data = list(data)
# print(data)
temp = []
full = 0

cal(0)