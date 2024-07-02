def recur(idx):
    if idx == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            recur(idx+1)
            arr.pop()

n, m = map(int,input().split())
arr = []
recur(0)