# ECOTE P.96
# 3-3 숫자 카드 게임

def solution (n):
    result = 0
    for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(min_value, result)

    return result


n, m = map(int, input().split())
print(solution(n))
