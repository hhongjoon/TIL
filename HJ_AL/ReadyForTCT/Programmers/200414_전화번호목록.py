def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if len(i)>len(j):
                continue
            tmp = j[:len(i)]

            if tmp == i:
                return False

    answer = True
    return answer

print(solution(["119", "97674223", "1195524421"]))