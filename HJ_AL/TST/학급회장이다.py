def main():

    N = int(input())

    p1=[]
    p2=[]
    p3=[]
    for i in range(N):
        s1, s2, s3 = map(int,input().split())
        # print(s1,s2,s3)
        p1.append(s1)
        p2.append(s2)
        p3.append(s3)

    result_score = max(sum(p1),sum(p2),sum(p3))
    








if __name__ == "__main__":
    main()