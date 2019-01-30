# import sys
# sys.stdin = open("view_input.txt")
T = 1   #test 횟수
for tc in range(T):
   ans = 0
   result = 0
   N =int(input())
   data = list(map(int, input().split()))
   print(data)
   for i in range(2, len(data)-1):
       print(i + 2)
       if data[i] >= data[i-2] + 1 and data[i] >= data[i-1] + 1 and data[i] >= data[i+1] + 1 and data[i] >= data[i+2] + 1:

           ans = data[i] - max(data[i-2], data[i-1], data[i+1], data[i+2])
           result += ans


   print("#{} {}".format(tc+1, result))