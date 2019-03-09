def checknum(n):
    if n == 3:
        return 10000000000,3
    elif n ==2:
        return 1000,2
    else:
        return 1 ,1

def main():
    T = int(input())
    table = [ [0]*2 for i in range(3) ]
    # print(table)
    for i in range(T):
        data = list(map(int,input().split()))
        for j in range(len(data)):
            big, small = checknum(data[j])
            table[j][0] += big
            table[j][1] += small
    print(table)
    maxval = -1
<<<<<<< HEAD
    count = 0
    for i in range(len(table)):
        if maxval<=table[i][0]:
            if maxval == table[i][0]:
                count+=1
            maxval = table[i][0]
            realval = table[i][1]
            who = i
    if count >=2:

    print(who+1,realval)
=======
    flag = False
    for i in range(3):

        if table[i][0] >= maxval:
            if table[i][0] == maxval:
                temp = maxval
                flag = True

            maxval = table[i][0]
            realval = table[i][1]
            who = i+1

    if flag and temp == maxval:
        print(0,realval)
    else:
        print(who, realval)

>>>>>>> 803676194e5560a1498b999a6464fb9e27911c2c


if __name__ =="__main__":
    main()