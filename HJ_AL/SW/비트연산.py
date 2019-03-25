def Bbit_print(i):
    output = ""
    for j in range(7,-1,-1):
        output += "1" if & (1 << j) else "0"
    print(output)

a = 0x86
key = 0xAA

print("a    ==> ", end= " ")
Bbit_print(a)