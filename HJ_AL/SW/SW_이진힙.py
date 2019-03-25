import sys
sys.stdin=open("이진 힙.txt")

def cal_heap(num,ea):
    for i in range(1,ea+1):
        if heap[i] == 0:
            heap[i] = num
            idx = i
            break

    while idx//2 > 0:
        if heap[idx] <heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx = idx//2
        else:
            break
    # print(heap)
def find_result(ea):
    sum = 0
    while ea//2>=1:
        ea = ea // 2
        sum += heap[ea]

    return sum




T = int(input())
for _ in range(T):
    ea = int(input())
    nums = list(map(int,input().split()))
    heap = [0]*(ea+1)
    for i in range(1,ea+1):
        num = nums[0]
        del nums[0]
        cal_heap(num,ea)

    # print(heap)
    print("#{} {}".format(_+1,find_result(ea)))
