# ECOTE P.312
# 11-2 곱하기 혹은 더하기

def solution(numbers):
    result = 1
    sum_count = 0

    for number in numbers:
        number = int(number)

        # 1 or 0 은 덧셈
        if number == 1 or number == 0:
            sum_count += number

        # 나머지는 곱셈
        else:
            result *= number

    return result + sum_count


numbers = str(input())
print(solution(numbers))
