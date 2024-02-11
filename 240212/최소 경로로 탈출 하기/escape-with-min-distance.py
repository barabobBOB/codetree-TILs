from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(M)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited[x][y] = True
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

    return graph[-1][-1] - 1

print(bfs(0, 0))