n = int(input())

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 1

def pb(x):
    if x < 3:
        return dp[x]
    dp[x] = pb(x - 1) + pb(x - 2)
    return dp[x]

print(pb(n))