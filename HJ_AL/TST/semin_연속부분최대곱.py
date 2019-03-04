n = int(input())
data = [float(input()) for i in range(n)]

print(data)

max_product = 1
now = 1
count = 0
for i in range(n):

    if now*data[i] < 1:
        now = 1
    else:
        if now*data[i] > max_product:
            max_product = now*data[i]
        now = now*data[i]

if max_product > 1:
    print('%.3f' % max_product)
else:
    print('%.3f' % max(data))
# if max_product > 1:
#     print(round(max_product, 3))
# else:
#     print(round(max(data), 3))

# print(f'{3.4567:.3f}')
# print(f'{3.4:.3f}')
print('%.3f' % 3.4567)
print('%.3f' % 3.4)
print('{0:.3f}'.format(3.4567))
print('{0:.3f}'.format(3.4))
