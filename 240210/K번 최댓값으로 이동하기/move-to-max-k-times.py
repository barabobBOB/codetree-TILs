import collections

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 위치 (입력은 1-based, 처리는 0-based)
r, c = map(int, input().split())
r, c = r - 1, c - 1

# 이동할 수 있는 방향 정의
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
NOT_EXISTS = (-1, -1)

for _ in range(k):
    visited = [[False] * n for _ in range(n)]
    bfs_q = collections.deque([(r, c)])
    visited[r][c] = True
    target_num = grid[r][c]
    best_pos = NOT_EXISTS
    
    while bfs_q:
        x, y = bfs_q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] < target_num:
                visited[nx][ny] = True
                bfs_q.append((nx, ny))
                
                # 우선순위 판단 및 업데이트
                if best_pos == NOT_EXISTS or (grid[nx][ny], -nx, -ny) > (grid[best_pos[0]][best_pos[1]], -best_pos[0], -best_pos[1]):
                    best_pos = (nx, ny)
    
    # 움직일 수 있는 곳이 없으면 종료
    if best_pos == NOT_EXISTS:
        break
    
    # 위치 업데이트
    r, c = best_pos

# 최종 위치 출력 (출력은 1-based)
print(r + 1, c + 1)