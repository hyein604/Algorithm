A, B = map(str, input().split())

N = int(A[-1] + A[-2] + A[-3])
M = int(B[-1] + B[-2] + B[-3])

print(max(N, M))