# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

#index를 1번 부터 사용하기 위해 m+1만큼 할당합니다.
graph = [[] for _ in range(n + 1)]

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    # 각 정점이 서로 이동이 가능한 양방향 그래프이기 때문에
    # 각 정점에 대한 간선을 각각 저장해줍니다.
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(n + 1)]
cnt = 0

def dfs(n):
    global cnt

    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)
    
dfs(1)

print(cnt)