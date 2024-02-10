from collections import deque

N, K, U, D = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

max_city = 0

def bfs(x, y):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    q = deque()
    q.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    while q:
        x, y = q.popleft()
        h = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                continue
            
            h = abs(h - graph[nx][ny])

            if U <= h <= D:
                visited[nx][ny] = True
                q.append((x, y))
                count += 1

    return count

for i in range(N):
    for j in range(N):
        max_city = max(bfs(i, j), max_city)

print(max_city)