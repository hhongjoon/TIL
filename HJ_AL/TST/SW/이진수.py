pattern = [
    '0000',
    '0001',
    '0010',
    '0011',
    '0100',
    '0101',
    '0110',
    '0111',
    '1000',
    '1001',
    '1010',
    '1011',
    '1100',
    '1101',
    '1110',
    '1111',

]
T = int(input())
for _ in range(T):
    ea, nums = map(str, input().split())
    print('#{} '.format(_+1),end="")
    for i in nums:
        if ord(i)-ord('0') > 9:
            # print(ord(i) - ord('A'))
            print(pattern[ord(i)-ord('A')+10], end="")
            continue
        print(pattern[ord(i)-ord('0')], end="")
    print()

