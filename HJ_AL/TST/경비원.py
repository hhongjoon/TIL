col, row = map(int,input().split())
T = int(input())
mat = [0]*((col+row)*2)
print(mat)

for i in range(1,T+1):
    dir , size = map(int,input().split())
    info_table = [0, size, col + row + size, col + row + col + size, col + size]
    mat[info_table[dir]] = i

dir, size = map(int,input().split())
s_idx = info_table[dir]
mat[s_idx] = 'start'
print(mat)
result=[]
for i in range(1,T+1):
    idx = mat.index(i)
    if abs(s_idx - idx) <= col+row:
        result.append(abs(s_idx - idx))
    else:
        result.append((col+row) - abs(s_idx - idx))
print(sum(result))



