#1
numbers = [2, 3, 6, 11, 8]

for i in numbers:
    print(i, end=" ")


print()

#2
odd = list()
even = list()

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)


ko = 'King of Night'
gaga = 'aaa'
print (gaga+ko)