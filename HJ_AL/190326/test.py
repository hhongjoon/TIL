def aaa(order):
    order.append(0)
    return order

nums = [1,2,3]
nums = list(map(str,nums))

print(nums)
nums = int("".join(nums))
print(nums)

