#바텀업디피
N = int(input())
interview = [list(map(int,input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for idx in range(N)[::-1]:    # [::-1] : 역행한다는 뜻
    if idx + interview[idx][0] > N:     # if idx > N: return -999999999
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1],
                      dp[idx + 1])

print(max(dp))