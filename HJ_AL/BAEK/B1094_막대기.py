#64cm
X = int(input())
sticks=[64]
while True:
    if sum(sticks) > X:
        minstick = min(sticks)
        sticks.remove(minstick)
        if minstick/2 + sum(sticks) >= X:
            sticks.append(minstick/2)
        else:
            sticks.append(minstick / 2)
            sticks.append(minstick/2)
    if sum(sticks) == X:
        print(len(sticks))
        break






