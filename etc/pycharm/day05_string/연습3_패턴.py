

def bruteforce_pattern(p,t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return i-len(p)
    else:
        return -1


p = 'is'
t = "this is a book"

print(bruteforce_pattern(p,t))