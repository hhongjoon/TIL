print(int(input()))
a,b = map(int,input().split())
print(a,b)
for i in range(5):
    inp = list(map(int,input()))
    for j in inp:
        print(j,end="")
    print()
