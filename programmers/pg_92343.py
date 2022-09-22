# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# 양과 늑대


def solution(info, edges):

    def find_adj(current_node):
        adj = []
        for edge in edges:
            if edge[0] == current_node:
                adj.append(edge[1])

        return adj

    def check(sheep, wolf):
        if sheep <= wolf:
            return False
        else:
            return True

    def dfs(sheep, wolf, start_node, visited):
        if info[start_node] == 0:
            sheep += 1
        else:
            wolf += 1

        if not check(sheep, wolf):
            return 0   # 늑대가 다 잡아먹었을 때

        max_count = sheep

        # 자식 dfs

        for v in visited:
            for adj in find_adj(v):
                if adj not in visited:
                    visited.append(adj)
                    max_count = max(max_count, dfs(sheep, wolf, adj, visited))
                    visited.pop()

        return max_count

    edges.sort()
    visited = [0]
    answer = dfs(0, 0, 0, visited)
    return answer


edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]



print(edges)