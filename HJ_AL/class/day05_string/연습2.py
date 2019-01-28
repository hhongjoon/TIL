def my_itoa(num):         # 정수를 문자열로.
    L = []
    a=999999
    while a != 0:
        a, b = divmod(num,10)
        #print(chr(b+ord('0')))  # ord: 문자->아스키코드,   chr: 숫자->문자
        L.insert(0,chr(b+ord('0')))
        num = a
    print(L)

    result = "".join(L)
    return result


print(my_itoa(897))