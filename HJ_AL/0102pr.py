#벌집계산 

# count = 1
# count2 = 0
# for i in range(1,10001):
    
#     for j range(1,6*count+1)
#         if i == 1:
#             k = str(count) + "aa"
#             k = list()
#             k.appand(i)
#             count = count + 1
#             continue

#       print(k)
input = input()
input = int(input)
count = 1
while input > 0:
   if input == 1:
       break
   input = input - 6*count
   count = count + 1 

print(count)