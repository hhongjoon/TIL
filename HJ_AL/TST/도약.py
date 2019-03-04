import time
def main():
    T = int(input())
    leaf = []
    for i in range(T):
        leaf.append(int(input()))
    leaf.sort()
    count = 0
    for i in range(len(leaf)-2):
        for j in range(i+1,len(leaf)-1):
            for k in range(j+1,len(leaf)):
                # print(leaf[i],leaf[j],leaf[k])
                step2 = leaf[k] - leaf[j]
                if step2 < 2:
                    continue
                step1 = leaf[j] - leaf[i]
                if step2 <2:
                    continue


                if step1 <= step2 and step2 <= step1 *2:
                    # print(leaf[i],leaf[j],leaf[k], 'answer')
                    count +=1

    print(count)



if __name__ == "__main__":
    st = time.time()
    main()
    end = time.time()
    print(end-st)