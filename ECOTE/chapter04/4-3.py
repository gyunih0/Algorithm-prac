# This is Coding Test P.115
# 왕실의 나이트

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

count = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)