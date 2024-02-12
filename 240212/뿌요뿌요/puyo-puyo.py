N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0

def dfs(x, y, k):
    visited[y][x] = True
    count = 1  # Start counting from the current node

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == k:
            count += dfs(nx, ny, k)  # Accumulate the count from recursive calls

    return count

c = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt = dfs(j, i, graph[i][j])  # Call DFS for each unvisited node
            if cnt >= 4:
                c += 1
            max_count = max(max_count, cnt)  # Update the max count if needed

print(c, max_count)