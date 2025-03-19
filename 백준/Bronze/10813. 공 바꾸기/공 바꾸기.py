N, M = map(int, input().split())
ball = [num for num in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    switch_first_number = ball[i-1]
    switch_second_number = ball[j-1]

    ball[i-1] = switch_second_number
    ball[j-1] = switch_first_number

print(* ball)