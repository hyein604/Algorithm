N = int(input())
arr = [0,1]
for i in range(N):
    arr.append(arr[i]+arr[i+1])
print(arr[N])