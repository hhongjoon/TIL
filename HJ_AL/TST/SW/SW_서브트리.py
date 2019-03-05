def preorder(given):
    global count
    count += 1
    if path.get(given) is None:
        return

    if len(path[given]) > 0:
        for i in path[given]:
            preorder(i)

T = int(input())

for _ in range(T):
    N, given = map(int,input().split())
    input_nums = list(map(int,input().split()))
    # print(input_nums)

    path = {}
    for i in range(len(input_nums)):
        if i %2 ==0:
            if path.get(input_nums[i]) is None:
                path[input_nums[i]] = [input_nums[i+1]]
            else:
                path[input_nums[i]].append(input_nums[i+1])
    # print(path)
    count = 0
    preorder(given)
    print("#{} {}".format(_+1,count))
