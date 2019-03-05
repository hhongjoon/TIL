
def get_loc(row,col,loc):
    base = 0
    level = 0
    while True:
        if row == 1 or col == 1:
            order = loc -base
            print(level,row,col,order)  # 여기 풀 것
            if row == 1:
                return level+1,
            if col == 1:
                return

            pass
        else:  # 둘 다 1 은 아님
            prev_base = base
            base += (row+col)*2 - 4
            if loc >base:
                row -= 2
                col -= 2
                level+=1
                continue
            else: # 자리값 구해야함
                order = loc - prev_base
                if order <= col:
                    return level + 1, order+level

                elif order-col +1 <= row:
                    return order-col +1+level, col+level

                elif order-col-row+2 <=col:
                    return row+level,  col -(order-col-row+2) +1+level

                else: # 마저 작성
                    return (row-2) - (order-(col+row+col-2)) +2 + level , level +1


def main():
    row, col = map(int,input().split())
    size = row*col
    loc = int(input())
    if loc > size:
        print(0)
        return
    print(get_loc(row,col,loc))





if __name__ =="__main__":
    main()