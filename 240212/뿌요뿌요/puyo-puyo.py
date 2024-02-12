N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0
count = 0

def dfs(x, y, k):
    visited[y][x] = True
    global count

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == k:
            count += 1
            dfs(nx, ny, k)

    return count + 1

c = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt = dfs(i, j, graph[i][j])
            count = 0
            if cnt >= 4:
                max_count = max(max_count, cnt)
                c += 1

print(c, max_count)