N, M = map(int, input().split())
number = list(map(int, input().split()))

# 구간합 배열 만들기
sum = [0]
for i in range(len(number)):
    sum.append(sum[i]+number[i])

for i in range(M):
    a, b = map(int, input().split())
    print(sum[b] - sum[a-1])