n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
arr = []

def recur(idx):
    if len(arr) == m:
        print(*arr)
        return

    for i in number:
        if i not in arr:
            arr.append(i)
            recur(idx+1)
            arr.pop()

recur(1)