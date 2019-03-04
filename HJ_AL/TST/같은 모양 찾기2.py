def make90(pattern, p_size):
    newpattern = []
    for i in range(p_size):
        temp=[]
        for j in range(p_size-1,-1,-1):
            temp.append(pattern[j][i])
        newpattern.append(temp)
    # print(newpattern)
    return newpattern

def isok(p_size,temp_pattern,temp_i,temp_j):
    for a in range(p_size):
        for b in range(p_size):
            if mat[temp_i+a][temp_j+b] != temp_pattern[a][b]:
                return False
    # print(temp_i,temp_j)
    return True

def check_pattern(sum,size,p_size,t_pattern):
    for i in range(0, size - p_size + 1):
        for j in range(0, size - p_size + 1):
            # print(i,j)
            if isok(p_size, t_pattern, i, j):
                sum += 1
    return sum


size = int(input())
mat = [ list(map(int,input())) for i in range(size) ]
# print(mat)
p_size = int(input())
pattern =[  list(map(int,input())) for i in range(p_size)  ]
pattern90 = make90(pattern,p_size)
pattern180 = make90(pattern90,p_size)
pattern270 = make90(pattern180,p_size)


sum = 0
sum = check_pattern(sum,size,p_size,pattern)
sum = check_pattern(sum,size,p_size,pattern90)
sum = check_pattern(sum,size,p_size,pattern180)
sum = check_pattern(sum,size,p_size,pattern270)
print(sum)


