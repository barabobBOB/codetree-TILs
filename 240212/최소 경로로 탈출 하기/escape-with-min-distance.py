from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):  # N행의 입력을 받음
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]  # N행 M열로 visited 초기화

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx, ny))

    return graph[-1][-1] - 1 if graph[-1][-1] != 1 else -1 

result = bfs(0, 0)
print(result)