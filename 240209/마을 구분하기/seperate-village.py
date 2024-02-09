def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[y][x] or gragh[y][x] == 0:
        return 0
    
    visited[y][x] = True
    
    count = 1
    
    count += dfs(x + 1, y)  
    count += dfs(x - 1, y) 
    count += dfs(x, y + 1) 
    count += dfs(x, y - 1) 
    
    return count

n = int(input())
gragh = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

result_person = []
vilige_cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and gragh[i][j] == 1:
            c = dfs(j, i)
            if c > 0:  
                result_person.append(c)
                vilige_cnt += 1

print(vilige_cnt)
result_person.sort()
for i in result_person:
    print(i)