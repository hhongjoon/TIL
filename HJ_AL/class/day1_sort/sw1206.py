import sys
sys.stdin = open("sw1206_input.txt")
def building_window(aparts):
    count = 0
    for i in range(len(aparts)):
        #print(i)
        a = b = c= d = 0
        if i-2 >= 0 :
            a = aparts[i-2]
        if i-1 >= 0 :
            b = aparts[i-1]
        if i+1 <= len(aparts)-1:
            c = aparts[i+1]
        if i+2 <= len(aparts)-1:
            d = aparts[i+2]
        if aparts[i] > a and aparts[i] > b and aparts[i] > c and aparts[i]>d:
            maax = max(a, b, c, d)
            count = count + (aparts[i] - maax)

    return count

def main():
    
    for i in range(10):
        cout = int(input())
        case = list(map(int, input().split()))
        print(f"#{i+1} {building_window(case)}")

if __name__ == "__main__":
    main()