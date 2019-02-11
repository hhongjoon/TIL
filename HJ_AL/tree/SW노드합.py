# import sys
# sys.stdin = open("nodesum_input.txt")

def sum_node(result, goal):
    for i in range(len(result),0,-1):
        # print(i-1, result)
        result[i//2 -1] += result[i-1]
    return result[goal-1]


T = int(input())
for _ in range(T):
    node, leaf, goal = map(int,input().split())
    result = [0 for i in range(node)]
    for i in range(leaf):
        num, val =map(int,input().split())
        result[num-1]=val

    print(f"#{_+1} {sum_node(result,goal)}")

