N = int(input())
for i in range(1, N+1):
    n = str(i)
    a, b = map(int, input().split())
    print("Case #" + n + ":", a+b)