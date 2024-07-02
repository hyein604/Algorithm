# 바텀업 DP
n, k = map(int, input().split())
item = [[0,0]]
for i in range(n):
    a,b = map(int, input().split())
    item.append([a,b])

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for idx in range(1, n+1):
    for weight in range(1, k+1):

        if weight < item[idx][0]:
            dp[idx][weight] = dp[idx-1][weight]
        else:
            dp[idx][weight] = max(dp[idx - 1][weight - item[idx][0]] + item[idx][1],
                                  dp[idx - 1][weight])
            
print(dp[n][k])