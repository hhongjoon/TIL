def solution(operations):

    temp = []
    for i in operations:
        command, num = i.split()
        if command == "I":
            temp.append(int(num))
            continue
        if command == "D":
            if len(temp) == 0:
                continue
            if num == "-1":
                minn = min(temp)
                temp.remove(minn)
            else:
                maxx = max(temp)
                temp.remove(maxx)

    if len(temp)>0:
        answer = [max(temp), min(temp)]
    else:
        answer = [0,0]

    return answer

print(solution(["I 7","I 5","I -5","D -1"]))

print(solution(["I 16","D 1"]))