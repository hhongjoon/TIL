import sys
sys.stdin = open("forth.txt")

def cal(case):
    for i in case:
        if i.isdigit():
            num_stk.append(int(i))
            continue
        else:

            if i == '.':
                if len(num_stk) > 1:
                    return 'error'
                return num_stk[-1]
            if len(num_stk)<2:
                return 'error'

            if i == '+':
                num_stk[-2] = num_stk[-2] + num_stk[-1]
            elif i == '-':
                num_stk[-2] = num_stk[-2] - num_stk[-1]
            elif i == '*':
                num_stk[-2] = num_stk[-2] * num_stk[-1]
            else:
                if num_stk[-1] == 0:
                    return 'error'
                num_stk[-2] = int(num_stk[-2] / num_stk[-1])

            del num_stk[-1]
    return 'error'

T = int(input())
for _ in range(T):
    input_case = list(map(str,input().split()))
    num_stk = []
    print(f"#{_+1} {cal(input_case)}")