answer = []
def dfs(mapp, path, N):
    val = path[-1]
    if len(path) == N:
        global answer
        path_t = path[:]
        answer.append(path_t)
        return
    else:

        for num,i in enumerate(mapp.get(val)):
            arr = i
            path.append(arr)
            mapp.get(val).pop(num)
            ret = dfs(mapp,path,N)
            mapp.get(val).insert(num,i)
            path.pop()
            if ret:
                return ret

def solution(tickets):

    mapp={}
    for i in tickets:
        if i[0] in mapp:
            mapp.get(i[0]).append(i[1])
        else:
            mapp[i[0]] = [i[1]]
    for i in mapp:
        mapp[i].sort()
    print(mapp)

    dfs(mapp,["ICN"],len(tickets)+1)

    return answer[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))