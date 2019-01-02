# dict = {
#     "대전": 23,
#     "서울" : 30,
#     "구미" : 20
# }
# aa = dict.values()   # 클래스형식
# print(list(aa))
# print(type(dict.values()))

# 1. 평균구하기

#print(sum(val))     # 클래스에  쌓여있어도  sum 가능
# sum = 0
# for i in val:
#     sum = sum + i

# #1_2
# score = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }

# val = score.values()

# print (sum(val) / len(val))

# 반평균 구하기
scores = {
    "철수":{
        "수학": 80,
        "국어" : 90,
        "음악" : 100
    },
    "영희":{
        "수학":70,
        "국어": 60,
        "음악": 50
    }
}

#print(scores["철수"])


# sum_sub = 0
# sum_per = 0

# for i in scores.values():
#     #print(i)
    
#     for j in i.values():
#         #print(j)
#         sum_sub += j
    
#     a = sum_sub /len(i.values())
#     #print(a)
    
#     sum_per += a
#     sum_sub = 0
    
# print(sum_per/len(scores))

# suum = 0
# for ii in scores.values():
#     print(ii)
#     suum = suum + (sum(ii.values())/len(ii))

# print(suum/len(scores))
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# total_score = 0
# count = 0
# for person_score in scores.values():
#     for individual_score in person_score.values:
#         total_score += individual_score
#         count +=1

# print(total_score/count)

#@@@@
# for key,value in scores.items():  #items 꼭 써야함
#     print(key)
#     print(value)

#3. 도시중에 최근 3일 중 가장 추웠던 곳, 가장 더웠던 곳

cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

max_temp = -500
min_temp = 500
for name, temp in cities.items():
    #print(max(temp))
    if max(temp) > max_temp:
        max_temp = max(temp)
        max_name = name
    if min(temp) < min_temp:
        min_temp = min(temp)
        min_name = name


print("가장 추운 지역은 {}입니다.(온도 : {})".format(min_name,min_temp))
print("가장 따듯한 지역은 {}입니다. (온도 : {})".format(max_name, max_temp))


f
