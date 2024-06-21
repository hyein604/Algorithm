n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

idx = 0
while idx != n:
    for i in range(idx,n):
        tmp = arr[i]
        for j in range(i+1,n):
            tmp += arr[j]
            if tmp == m:
                answer += 1
                break
            elif tmp < m:
                continue
            else:
                break
        idx += 1
answer += arr.count(m)

print(answer)