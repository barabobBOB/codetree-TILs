from collections import deque
from itertools import combinations

N, K, U, D = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs(start):
    visited = [[False] * N for _ in range(N)]
    count = 1  # 시작 도시 포함

    q = deque([start])
    visited[start[0]][start[1]] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                h_diff = abs(graph[x][y] - graph[nx][ny])
                if U <= h_diff <= D:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

max_count = 0
all_positions = [(i, j) for i in range(N) for j in range(N)]

for combo in combinations(all_positions, K):
    total = 0
    for pos in combo:
        total += bfs(pos)
    max_count = max(max_count, total)

print(max_count)