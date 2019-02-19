import sys
sys.stdin = open("계산기3.txt")
# (9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2))

def cal(operator):
    global nums
    global operators
    temp_oper = len(operator)
    temp_nums = len(nums)
    templist_nums = nums[temp_nums-(temp_oper+1):]  # 계산 유효 숫자
    original_templist = len(templist_nums)
    for i in range(temp_oper):
        if operator[i] == "+":
            templist_nums[1] = templist_nums[0] + templist_nums[1]

        else : # '-'일 때
            templist_nums[1] = templist_nums[0] - templist_nums[1]

        del templist_nums[0]
        #del operators[-1]

    nums = nums[0:len(nums)-original_templist] + templist_nums
    operators = operators[:len(operators)-(temp_oper+1)]


    while len(operators)>0 and operators[-1] in mul_div:
        if operators.pop() == "*":
            nums[-2] = nums[-2]*nums[-1]

        else:
            nums[-2] = nums[-2] / nums[-1]

        del nums[-1]



def make_post(form):
    for i in range(len(form)):
        # global operators
        # print(operators)
        # print(nums)
        # print()

        if form[i].isdigit():
            nums.append(int(form[i]))
            if operators[-1] in mul_div:
                chr = operators.pop()
                if chr == "*":
                    nums[-2] = nums[-2] * nums[-1]
                else:
                    nums[-2] = nums[-2] / nums[-1]
                del nums[-1]


            continue
        else:
            if form[i] == ")":
                for j in range(len(operators)-1,-1,-1):
                    if operators[j] == '(':
                        cal(operators[j+1:])
                        break

            else:

                operators.append(form[i])








for _ in range(10):
    size = int(input())
    formula = list(input())
    #print(formula)

    operators = []
    nums = []
    mul_div = ['*','/']
    make_post(formula)
    #print(operators)
    print(f"#{_+1} {nums[0]}")