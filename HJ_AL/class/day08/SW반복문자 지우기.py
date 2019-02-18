import sys
sys.stdin = open("반복문자지우기.txt")

def solve(data,stack):
    for i in data:
        stack.append(i)
        if len(stack)>1 and stack[-1] == stack[-2]:
            stack = stack[:len(stack)-2]
    return len(stack)



T = int(input())

for _ in range(T):
    input_str = input()
    stack = []
    print(f"#{_+1} {solve(input_str,stack)}")
