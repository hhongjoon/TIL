#연속 최대 합

def main():
    T = int(input())
    dotories = list(map(int,input().split()))
    result = 0
    result_list = []

    allminus = True
    for i in dotories:
        if i > 0:
            allminus = False
            break
    if allminus:
        print(max(dotories), max(dotories))
        return

    for i in dotories:
        prev = result
        if prev + i > 0:
            if i < 0:
                result_list.append(prev)
            result = prev + i
        else:
            result_list.append(prev)
            result=0
    result_list.append(result)
    babo = max(result_list)

    ddok = 0
    for i in dotories:
        if i > 0:
            ddok+=i

    print(babo, ddok)


if __name__ == "__main__":
    main()
