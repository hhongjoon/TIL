import sys
sys.stdin = open("특별한정렬_input.txt")
def selection_sort(aa):
    for i in range(0, len(aa)-1):
        for j in range(i+1, len(aa)):
            if aa[i] > aa[j]:
                aa[i], aa[j] = aa[j], aa[i]

T = int(input())
for _ in range(T):
    list_ea = int(input())
    list_og = list(map(int, input().split()))
    selection_sort(list_og)

    result = []
    pivot = 1
    for __ in range(len(list_og)):
        if pivot == 1:
            result.append(str(list_og.pop()))
            pivot = 0
        else:
            result.append(str(list_og.pop(0)))
            pivot = 1

        if len(result) == 10:
            break
    a = ' '.join(result)

    print(f"#{_+1} {' '.join(result)}")




