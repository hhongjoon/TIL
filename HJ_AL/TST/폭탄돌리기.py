def passbomb(time, answer,basetime,who):
    time = int(time)             ## 시간 먼저 더하고 210 이상이면 탈락
    basetime += time
    if basetime > 210: 
        return 0, who, basetime

    if answer == 'F' or answer == 'P':
        return 1, who ,basetime

    else:
        who=who+1
        if who ==9:
            who = 1
    return 1, who, basetime


def main():

    havebomb = int(input())
    quiz = int(input())
    basetime = 0
    for i in range(quiz):
        time, answer = input().split()
        check, havebomb, basetime = passbomb(time,answer,basetime,havebomb)
        # print(havebomb)
        if check == 0:
            print(havebomb)
            return
    print(havebomb)


if __name__ =="__main__":
    main()