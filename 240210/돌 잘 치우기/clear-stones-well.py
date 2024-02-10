from itertools import combinations
from collections import deque

def bfs(grid, starts):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    queue = deque(starts)
    count = 0

    for x, y in starts:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        count += 1

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return count

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

stones = [(x, y) for x in range(n) for y in range(n) if grid[x][y] == 1]

max_count = 0
# 가능한 조합 생성
for stones_to_remove in combinations(stones, m):
    
    # 조합에서 돌 삭제
    for x, y in stones_to_remove:
        grid[x][y] = 0

    # 해당 그래프로 bfs 시작
    count = bfs(grid, starts)

    # 가장 큰 값
    max_count = max(max_count, count)
    
    # 원상 복구
    for x, y in stones_to_remove:
        grid[x][y] = 1

print(max_count)