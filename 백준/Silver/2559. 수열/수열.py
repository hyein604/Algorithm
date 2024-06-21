N,K = map(int,input().split())
temp = list(map(int,input().split()))
answer = []
tmp = 0

for i in range(K):
    tmp += temp[i]
answer.append(tmp)

for i in range(N-K):
    tmp = tmp + temp[K+i] - temp[i]
    answer.append(tmp)

print(max(answer))