from collections import deque
import enum

class Element(enum.Enum):
    WATER = 0
    GLACIER = 1
    
n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
elapsed_time = 0
last_melt_cnt = 0

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = True
    melt_this_round = set()
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == Element.WATER.value and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif a[nx][ny] == Element.GLACIER.value and not visited[nx][ny]:
                    melt_this_round.add((nx, ny))
    
    # 녹여야 할 빙하 녹이기
    for x, y in melt_this_round:
        a[x][y] = Element.WATER.value
    
    # 녹인 빙하의 개수 업데이트
    melted = len(melt_this_round)
    if melted == 0:
        break
    
    last_melt_cnt = melted
    elapsed_time += 1

print(elapsed_time, last_melt_cnt)