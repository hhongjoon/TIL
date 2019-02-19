# import sys
# sys.stdin = open("계산기3.txt")

def cal(operator):
    global nums
    temp_oper = len(operator)
    temp_nums = len(nums)
    templist_nums = nums[temp_nums-(temp_oper+2):]
    for i in range(len(temp_oper)):
        if temp_oper[i] == "+":
            templist_nums[1] = templist_nums[0] + templist_nums[1]
            del templist_nums[0]
        else :
            templist_nums[1] = templist_nums[0] - templist_nums[1]
            del templist_nums[0]
    nums = nums[0:len(nums)-len(templist_nums)] + templist_nums



def make_post(form):
    for i in range(len(form)):
        global operators
        print(operators)
        print(nums)
        print()

        if form[i].isdigit():
            nums.append(form[i])
            if operators[-1] in mul_div:
                chr = operators.pop()
                if chr == "*":
                    operators[-2] = operators[-2] * operators[-1]
                else:
                    operators[-2] = operators[-2] / operators[-1]
                del operators[-1]


            continue
        else:
            if form[i] == ")":
                for j in range(len(operators)-1,-1,-1):
                    if operators[j] == '(':
                        cal(operators[j+1:])

            else:
                operators.append(form(i))








for _ in range(10):
    size = int(input())
    formula = list(input())
    print(formula)

    operators = []
    nums = []
    mul_div = ['*','/']
    make_post(formula)
    print(operators)
    print(nums)