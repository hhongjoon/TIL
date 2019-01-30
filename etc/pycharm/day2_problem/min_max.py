import sys
sys.stdin = open("sample_input.txt")


def min_max(data, a, z):
    if a < z :

        copy = list(data)
        mid = int(a + z)/2

        # min_max(copy[:mid+1],0,mid)
        # min_max(copy[mid+1:],mid+1,len(copy)-1)
        min_max(copy, 0, mid)
        min_max(copy, mid + 1, len(copy) - 1)
        merge(copy,a,mid,z)

def merge(data, l, mid, r):
    result = []
    if data[l] > data[r]:
        data[l], data[r] = data[r],data[l]


def main():
    case = int(input())
    num = int(input())
    nums = list(map(float, input.split()))

    for i in nums:
        print(f"#{i + 1} {}")

if __name__ == "__main__":
    main()