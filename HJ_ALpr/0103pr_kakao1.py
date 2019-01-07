#입력
count = int(input())
#a, b = map(int,input().split())
#print(count)
#print(b)
val = []

for i in range(0,count):
    a, b = map(int,input().split())
    if a == 0:
        a_rank = 100
    if b == 0:
        b_rank = 100

    #경우 a
    a_count = 1
    while a > 0:
        if a - a_count <= 0:
            a_rank = a_count
            break
        a = a - a_count
        a_count += 1

    if a_rank >= 7:
        a_val = 0
    elif a_rank >= 6:  # 6등
        a_val = 100000
    elif a_rank >= 5:
        a_val = 300000
    elif a_rank >= 4:
        a_val = 500000
    elif a_rank >= 3:
        a_val = 2000000
    elif a_rank >= 2:
        a_val = 3000000
    elif a_rank >= 1:
        a_val = 5000000

    #print(f"a_rank 는 {a_rank} \n a_val = {a_val}")

    # 경우 b
    b_count = 1

    while b > 0:
        if b == 1 and b_count == 1:
            b_rank = 1
            break

        if b - 2**(b_count-1) <= 0:
            b_rank = b_count
            break

        b = b - 2**(b_count-1)
        b_count += 1

    if b_rank >= 6:
        b_val = 0
    elif b_rank >= 5:
        b_val = 2**5 * (10000)
    elif b_rank >= 4:
        b_val = 2**6 * (10000)
    elif b_rank >= 3:
        b_val = 2**7 * (10000)
    elif b_rank >= 2:
        b_val = 2**8 * (10000)
    elif b_rank == 1:
        b_val = 2**9 * (10000)


    #print(f"b_rank 는 {b_rank} \n b_val = {b_val}")

    #print(a_val + b_val)
    val.append(a_val+b_val)

for j in val:
    print(j)