n,m = map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
arr = []
def dp(idx):
    if len(arr) == m:
        print(* arr)
        return

    for i in numbers:
        if i >= idx:
            arr.append(i)
            idx = i
            dp(idx)
            arr.pop()

dp(0)