# import sys
# sys.stdin = open("도약난수.txt")
import time

def main():
    T = int(input())
    leaf = []
    for i in range(T):
        leaf.append(int(input()))
    leaf.sort()
    print(leaf)
    sum = 0
    for i in range(len(leaf)-2):
        for j in range(i+1,len(leaf)-1):

            k =  (len(leaf)-1 + j+1)//2
            step1 = leaf[j] - leaf[i]
            step2 = leaf[k] - leaf[j]
            if step2 > step1*2:

                while step2 > step1*2:
                    print(i,j,k,'idx')
                    prev = k
                    k = (k+ (j+1))//2
                    step2 = leaf[k] - leaf[j]
                    if k-j <2:
                        # prev = k
                        break


                for r in range(prev,len(leaf)-1):
                    print(leaf[i],leaf[j],leaf[r])
                    step2 = leaf[r] - leaf[j]
                    if step2 >= step1 and step2 <= step1*2:
                        print(leaf[i],leaf[j],leaf[r], 'ans')
                        sum += 1

            else:
                while step2 <= step1*2:
                    print(i,j,k,'idx')
                    prev = k
                    k = (len(leaf)-1 + k)//2
                    step2 = leaf[k] - leaf[j]


                    if k-j <2:
                        break


                for r in range(j+1,prev+1):
                    print(leaf[i],leaf[j],leaf[r])
                    step2 = leaf[r] - leaf[j]
                    if step2 >= step1 and step2 <= step1 * 2:
                        print(leaf[i],leaf[j],leaf[r],'ans')
                        sum += 1




    print(sum)



if __name__ == "__main__":
    st = time.time()
    main()
    end = time.time()
    print(end-st)