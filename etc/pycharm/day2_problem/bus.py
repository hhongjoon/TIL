import sys
sys.stdin = open("bus_input.txt")

def elec_bus(case):

    k, n, m = map(int, input().split())
    charge_loc = list(map(int, input().split()))

    car_bat = k  ## 배터리
    next = 999999999
    count = 0

    for i in range(0,n+1):

        if i == 0:
            for j in range(len(charge_loc) - 1, -1, -1):  ## 끝에있는 충전소부터 검색하여 현재위치로 부터 멀리있는 정류소 next에 저장
                if i<=charge_loc[j] and i+car_bat >= charge_loc[j]:
                    next = charge_loc[j]
                    #car_bat -= 1
                    break
        else:

            if i == next:  ## 다음 충전소
                if i == n:
                    return count
                car_bat = k  ## 충전
                count +=1
                for j in range(len(charge_loc) - 1, -1, -1):  ## 끝에있는 충전소부터 검색하여 현재위치로 부터 멀리있는 정류소 next에 저장
                    if i <= charge_loc[j] and i + car_bat >= charge_loc[j] and i+car_bat < n:
                        next = charge_loc[j]
                        break
                continue
            else:

                for j in range(len(charge_loc) - 1, -1, -1):  ## 끝에있는 충전소부터 검색하여 현재위치로 부터 멀리있는 정류소 next에 저장
                    if i <= charge_loc[j] and i + car_bat-1 >= charge_loc[j] and i+car_bat < n:
                        next = charge_loc[j]
                        break
                car_bat -= 1

                if car_bat == 0 and i!=n:
                    return 0

    return count

def main():
    tt = int(input())
    for i in range(tt):
        print(f"#{i+1} {elec_bus(tt)}")



if __name__ == "__main__":
    main()