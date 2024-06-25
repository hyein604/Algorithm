n, k = map(int, input().split())
arr = []
for _ in range(n):
    coin = int(input())
    if coin > k:
        break
    else:
        arr.append(coin)

count = 0

for i in range(len(arr)-1, -1, -1):
    count += k // arr[i]
    k = k % arr[i]
    if k == 0:
        break

print(count)