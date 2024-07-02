n,m = map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()
arr = []

def dp():
    if len(arr) == m:
        print(* arr)
        return

    for i in numbers:
        arr.append(i)
        dp()
        arr.pop()

dp()