# ECOTE P.99
# 3-4 1이 될 때까지

n, k = map(int, input().split())


def solution(n, k):
    count = 0
    while n != 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1

    return count

print(solution(n, k))

