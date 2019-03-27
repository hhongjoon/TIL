def upperSearh2(s,e,data):
    sol = -1
    while s<=e:
        if arr[m] < data:
            s = m+1
            sol = m

        else:
            e = m-1