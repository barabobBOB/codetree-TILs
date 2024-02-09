from collections import deque

N, K = map(int, input().split())
graph = []
start = []
result = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(K):
    start.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]

    q = deque()
    q.append((x, y))

    count = 0

    if not visited[y][x]:
        count += 1

    visited[y][x] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            
            if graph[ny][nx] == 1 or visited[ny][nx]:
                continue
            
            visited[ny][nx] = True
            q.append((nx, ny))
            count += 1

    return count

for i in start:
    result += bfs(i[0] - 1, i[1] - 1)

print(result)