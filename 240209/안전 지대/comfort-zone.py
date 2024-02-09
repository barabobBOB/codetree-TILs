# dfs 사용

N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

def dfs(x, y, k):
    if x > M - 1 or x < 0 or y > N - 1 or y < 0 or graph[y][x] <= k or visited[y][x]:
        return False
    
    visited[y][x] = True

    dfs(x, y - 1, k)
    dfs(x, y + 1, k)
    dfs(x - 1, y, k)
    dfs(x + 1, y, k)

    return True

K = 0
max_safe = 0

for k in range(1, 101):
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(M):
        for j in range(N):
            if not visited[j][i] and graph[j][i] > k:
                if dfs(i, j, k):
                    cnt += 1
    if max_safe < cnt:
        K = k
        max_safe = cnt

print(K, max_safe)