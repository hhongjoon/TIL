def get_primes():                       ## 소수 구하기 num_list에서 루트한 소수들로 나눠서 없앰
    for i in range(len(primes)):
        num = primes[i]
        for j in range(len(num_list)):
            if j >=len(num_list):
                break
            quot, remain = divmod(num_list[j],num)
            if quot>1 and remain == 0:
                del num_list[j]

    # print(num_list)


a,b = map(int,input().split())        ## 인풋
if a == 1:                          ## 1이라면 초기값 2로 설정
    a= 2
primes=[]
num_list = list(range(a,b+1))
prime_list = list(range(2,int(b**(1/2))+1))
# print(prime_list)
while len(prime_list)>0:          ## 루트씌운 기준 소수들 구하기 / 제곱근의 소수들로 전체를 나눠서 없애면 소수만 남음
    num = prime_list.pop(0)
    primes.append(num)
    for i in range(len(prime_list)):
        if i>=len(prime_list):
            break
        if prime_list[i] % num == 0:
            del prime_list[i]
# print(primes)
get_primes()
print(len(num_list))
print(num_list[0]+num_list[-1])
