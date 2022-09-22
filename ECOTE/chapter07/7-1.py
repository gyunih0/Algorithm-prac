# This is Coding Test P.187
# 순차 탐색 코드

def sequential_search(n, target, array):

    for i in range(n):

        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재 위치 반환


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))


