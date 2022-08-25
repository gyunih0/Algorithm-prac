# This is Coding Test P.113
# 시각

n = int(input())

# n 이 3, 13, 23 일때는 60 * 60 경우의 수
# 그 외에는 3, 13, 23, 30 ~ 39, 43, 53 (15가지)초 또는 분  -> (45 * 15) + (15 * 60)

# my_solution
include_3 = [3, 13, 23]
result = 0
for hour in range(n+1):
    if hour in include_3:
        result += 60 * 60
    else:
        result += (45 * 15 + 15 * 60)

print(result)

# solution
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
