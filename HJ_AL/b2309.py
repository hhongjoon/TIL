#일곱난쟁이
def dwarf7(kee):
    total = sum(kee)
    for i1 in range(9):
        for i2 in range(9):
            if i1 != i2 and i1<i2 :
                tt = kee[i1] + kee[i2]
                if total - tt == 100:
                    del kee[i2]
                    del kee[i1]
                    return sorted(kee)

data = [int(input()) for i in range(9)]
for i in dwarf7(data):
    print(i)