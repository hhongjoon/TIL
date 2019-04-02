dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
arr = []
T = int(input())
for tc in range(T):
    N = int(input())
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        arr.append((2*x, 2*y, d, k))
    counter = N;
    result = 0;
    while counter:
        print(arr)
        brr = []
        crr = set()
        cset = set()
        for atom in arr:
            x, y, d, k = atom
            x += dx[d];
            y += dy[d];
            brr.append((x, y, d, k))
            c = len(cset)
            cset.add((x,y))
            if c == len(cset):
                crr.add((x,y))
        arr.clear()
        for atom in brr:
            x, y, d, k = atom
            if (x,y) in crr:
                result += k
                counter -= 1
            elif max(x, y) > 2000 or min(x, y) < -2000:
                counter -=1
            else:
                arr.append(atom)
    # print(f"#{tc+1}", result)