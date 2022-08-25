# This is Coding Test P.110
# 상하좌우


x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

n = int(input())
moves = input().split()

for move in moves:
    x += dx[move_type.index(move)]
    y += dy[move_type.index(move)]

    # 공간 벗어나면 되돌리기 (무시)
    if x < 1 or y < 1 or x > n or y > n:
        x -= dx[move_type.index(move)]
        y -= dy[move_type.index(move)]

print(x, y)
