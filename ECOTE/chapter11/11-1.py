# ECOTE P.311
# 11-1 모험가 길드

n = int(input())
data = list(map(int, input().split()))

# 공포도 적은 순서대로 그룹 결성


def solution(n, data):
    data.sort()
    result = 0
    count = 0
    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0

    return result


print(solution(n, data))

