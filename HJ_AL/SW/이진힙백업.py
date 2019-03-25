def cal_heap(num):
    start = 1
    while True:
        if heap[start]==0:
            heap[start] = num
            print(heap)
            return
        else:
            if num > heap[start]: # 부모보다 클때, 내려가야함
                if heap[start*2] == 0:
                    start = start*2
                    continue
                if heap[start*2 + 1] == 0:
                    start = start*2 + 1
                    continue
                else:
                    start = start*2
                    continue


            else: # 부모보다 작을 때, 바꾼 후 기존의 값을 내림
                temp = heap[start]
                heap[start] = num
                num = temp
                if heap[start*2] == 0:
                    start = start*2
                    continue
                if heap[start*2 + 1] == 0:
                    start = start*2 + 1
                    continue
                else:
                    start = start*2
                    continue

T = int(input())
for _ in range(T):
    ea = int(input())
    nums = list(map(int,input().split()))
    heap = [0]*(ea+1)
    for i in range(1,ea+1):
        num = nums[0]
        del nums[0]
        cal_heap(num)