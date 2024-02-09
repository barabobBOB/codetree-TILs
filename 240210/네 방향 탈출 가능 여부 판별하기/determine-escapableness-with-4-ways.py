from collections import deque

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
    
        if x == M-1 and y == N-1:
            return 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[ny][nx] == 0:
                continue
            
            if not visited[ny][nx]:
                graph[ny][nx] = graph[y][x] + 1
                visited[ny][nx] = True
                queue.append((nx, ny))
        
    return 0
        
print(bfs(0, 0))