#괄호의 짝을 검사
result = []
in_chr = list(input())
#print(in_chr)
for i in in_chr:

    if i == '(':
        result.append('(')
    else:
        if len(result) ==0:
            break
        del result[-1]

if len(result) == 0 :
    print('True')
else:
    print('False')
