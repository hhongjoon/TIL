def main():   ## 원안에 사각형 몇개 들어가는지, 4등분 해서 한조각만 생각
    R = int(input())
    sum = 0
    if R == 1:
        print(1)
        return
    for i in range(1,R+1):
        for j in range(1,R+1):
            if i**2 + j**2 <=R**2:
                sum+=1
    print(sum * 4)

if __name__ =="__main__":
    main()