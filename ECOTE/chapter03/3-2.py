# ECOTE P.93
# 3-2 큰 수의 법칙

# N개의 수, 더해지는 횟수 M, 최대 연속 가능 K
n, m, k = map(int, input().split())

# Data 입력
data = list(map(int, input().split()))

def solution(data, m, k):
    data.sort()
    first = data[-1]
    second = data[-2]

    count = int(m / (k + 1)) * k
    count += m % (k+1)

    result = (first * count) + (second * (m - count))
    return result

print(solution(data, m, k))

