n, m = map(int, input().split())

nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

answer = 0

def is_happy_sequence():
    # 주어진 seq가 행복한 수열인지 판단하는 함수입니다.
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        max_ccnt = max(max_ccnt, consecutive_count)
    
    # 최대로 연속한 회수가 m이상이면 true를 반환합니다. 
    return max_ccnt >= m

# 가로
for i in range(n):
    seq = nums[i][:]
    
    if is_happy_sequence():
        answer += 1

# 세로
for j in range(n):
    for i in range(n):
        seq[i] = nums[i][j]

    if is_happy_sequence():
        answer += 1

print(answer)