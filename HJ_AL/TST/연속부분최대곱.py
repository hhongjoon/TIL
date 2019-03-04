def main():
    T = int(input())
    values = []
    for i in range(T):
        values.append(float(input()))

    result = 1
    prev_list = []
    for i in values:
        prev = result
        result *= i
        if result < 1:
            prev_list.append(prev)
            result = 1
            continue
        if prev > result:
            prev_list.append(prev)


    print(round(max(prev_list),3))



if __name__ == "__main__":
    main()