# This is Coding Test P.151
# 음료수 얼려 먹기

# N, M 입력
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    # 맵 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 해당 위치로 부터 상하좌우 탐색
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


# 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재위치에서 DFS
        if dfs(i,j) == True:
            result += 1


print(result)


