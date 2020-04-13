
#키패드
def sol(pw):
    if (isPattern(pw) and isCnt(pw) and isLine(pw)):
        return True

    return False


def isPattern(pw):
    bag = set()
    for i in range(2,7):
        for j in range(0,len(pw)-i+1):
            temp = pw[j:j+i:1]
            before = len(bag)
            bag.add(temp)
            after = len(bag)

            if before == after:
                return False
    return True


def isCnt(pw):
    for i in range(0,len(pw)):
        val = pw[i]
        tempInt = int(val)
        cnt[tempInt]+=1
        if cnt[tempInt] > 2:
            return False
    return True

def isLine(pw):
    for i in range(0,len(pw)):
        val = pw[i]
        lineList = pad.get(val)
        if val == "0" or val=="8":
            if (len(pw)-i < 4):
                continue
            numpiece = pw[i:i+4]
        elif(val=="5"):
            continue
        else:
            if (len(pw)-i < 3):
                continue
            numpiece = pw[i:i + 3]

        for j in lineList:
            if numpiece == j:
                return False
    return True


cnt = [0]*10

pad = dict()
pad["0"] = list()
pad["0"].append("0258")

pad["1"] = list()
pad["1"].append("123")
pad["1"].append("159")
pad["1"].append("147")

pad["2"] = list()
#pad["2"].append("258")


pad["3"] = list()
pad["3"].append("321")
pad["3"].append("369")
pad["3"].append("357")

pad["4"] = list()
pad["4"].append("456")

pad["6"] = list()
pad["6"].append("654")

pad["7"] = list()
pad["7"].append("789")
pad["7"].append("753")
pad["7"].append("741")

pad["8"] = list()
pad["8"].append("8520")

pad["9"] = list()
pad["9"].append("963")
pad["9"].append("987")
pad["9"].append("951")

print(sol("334455669"))