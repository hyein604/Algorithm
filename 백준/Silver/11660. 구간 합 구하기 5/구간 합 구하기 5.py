N, M = map(int,input().split())
tmp_n = [list(map(int,input().split())) for _ in range(N)]
numbers = [[0 for _ in range(N+1)] for _ in range(N+1)]
sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
# 입력받은 숫자 테이블 만들기
for i in range(1,N+1):
    for j in range(1,N+1):
        numbers[i][j] = tmp_n[i-1][j-1]
# 구간합 테이블 만들기
for i in range(1,N+1):
    for j in range(1,N+1):
        sum[i][j] = numbers[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

tmp_m = [list(map(int,input().split())) for _ in range(M)]

for i in range(M):
    answer = sum[tmp_m[i][2]][tmp_m[i][3]] - sum[tmp_m[i][2]][tmp_m[i][1]-1] - sum[tmp_m[i][0]-1][tmp_m[i][3]] + sum[tmp_m[i][0]-1][tmp_m[i][1]-1]
    print(answer)