n, m = map(int, input().split())
arr = []

def recur(idx):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(idx, n+1):
        if i not in arr:
            arr.append(i)
            recur(i+1)
            arr.pop()

recur(1)