#원카드 게임 / 카드 순서를 input받고 원카드 룰대로 흘러갈 수 있는지 판단

def sol(cards):

    for i in range(0,len(cards)-1):
        shape1, num1 = cards[i][0], cards[i][1]
        shape2, num2 = cards[i+1][0], cards[i+1][1]

        if shape1 != shape2 and num1 != num2:
            return False


    return True

print(sol(["S4", "H4","D4","D9","H9","H4","H2","S2"]))
print(sol(["S4", "H1","D4","D9","H9","H4","H2","S2"]))







