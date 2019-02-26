import sys
sys.stdin = open("피자.txt")

def solve(N):
    global pizzas
    in_oven = pizzas[:N]
    pizzas=pizzas[N:]
    while True:

        for i in  range(len(in_oven)):
            if len(pizzas) !=0 and in_oven[i][1] == 0:
                in_oven[i] = pizzas.pop(0)

        in_oven = [  [i[0],i[1]//2] for i in in_oven  ]

        #print(f"@{in_oven} ## {pizzas}")


        while len(pizzas) == 0:
            copyoven = in_oven[:]
            #print(in_oven, len(in_oven))
            pivot=0
            while True:
                if pivot == len(in_oven):
                    break
                if in_oven[pivot][1] == 0:
                    del in_oven[pivot]
                    continue
                pivot += 1
            if len(in_oven) == 0:
                return copyoven[-1][0]

            in_oven = [[i[0], i[1] // 2] for i in in_oven]


        #print(f"#{in_oven} ## {pizzas}")

T = int(input())
for _ in range(T):
    N , nums = map(int,input().split())
    indata = list(map(int,input().split()))
    pizzas = []
    for i in range(len(indata)):
        pizzas.append([i+1, indata[i]])

    #print(pizzas)
    print(f"#{_+1} {solve(N)}")
