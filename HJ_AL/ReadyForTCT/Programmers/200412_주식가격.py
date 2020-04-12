def solution(prices):
    temp = [0]*len(prices)
    piv = 0
    for i in range(len(prices)):
        val = prices[i]
        for j in range(i+1,len(prices)):
            if val <= prices[j]:
                temp[i]+=1
            else:
                temp[i] += 1
                break;


    answer = []
    return temp


print (solution([1,10,0,5,6,9,3]))