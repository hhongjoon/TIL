import sys
sys.stdin = open("괄호검사.txt")
def result(input_str,stack):
    for i in input_str:
        if i == "{" or i =="(":
            stack.append(i)
            continue
        if i == "}" or i ==")":
            if len(stack) == 0:
                return 0
                break


            if i =="}":
                temp = stack.pop()
                if temp =='(':
                    return 0
                    break
            else:
                stack.pop()
    if len(stack) >0:
        return 0

    return 1


T=int(input())
for _ in range(T):
    input_str = input()
    print(f"#{_+1}",end=" ")
    stack = []
    print(result(input_str,stack))

