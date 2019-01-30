def atoi(string):
    value = 0
    i = 0
    while (i< len(string)):
        c=string[i]
        if c>= '0' and c <='9':
            digit = ord(c) - ord('0')       ## 해당값의 아스키코드 반환
        else:
            break
        value = (value*10)+digit;
        i+=1
    return value

a='123456'
print(type(a))
b=atoi(a)
print(type(b))