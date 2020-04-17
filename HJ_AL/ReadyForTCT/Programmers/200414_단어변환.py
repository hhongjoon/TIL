# bfs 언제 탈출할지 고민 / visited {a:0, a:1 ...} / temp = [("wer",0), ("wee",2), ....]
def findnext(w, words):
    inWords = []
    for i in words:
        cnt = 0
        for j in range(len(w)):
            if w[j] != i[j]:
                cnt+=1
            if cnt == 2:
                continue
        if cnt == 1:
            inWords.append(i)

    return inWords
def bfs(b,t,words):
    visited = {}
    a = (b,0)
    temp = [a]

    while True:
        if len(temp) == 0:
            return 0
        val = temp.pop(0)
        inWords = findnext(val[0],words)

        for i in inWords:
            if visited.get(i,99999) > val[1]:
                visited[i] = val[1]+1
                temp.append((i,val[1]+1))
                if i == t:
                    return val[1]+1

def solution(begin, target, words):
    idx = [0]*len(words)
    answer = bfs(begin,target,words)

    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))