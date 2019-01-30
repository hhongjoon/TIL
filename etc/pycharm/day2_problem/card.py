import sys
sys.stdin = open("card_input.txt")

case = int(input())

for iii in range(case):
    n = int(input())
    cards = list(map(int,input()))
    count = {}
    for i in cards:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    max_value = -1
    #print(count)
    for key, val in count.items():
        if val >= max_value:
            if val == max_value:
                max_key = max(max_key,key)
            else:
                max_key = key
                max_value = val

    #print(count)
    print(f"#{iii+1} {max_key} {max_value}")

