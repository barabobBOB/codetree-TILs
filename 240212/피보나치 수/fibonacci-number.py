n = int(input())

dp = [0] * (n + 1)

def pb(x):
    if x <= 2:
        dp[x] = 1
    else:
        dp[x] = pb(x - 1) + pb(x - 2)
    return dp[x]

print(pb(n))