n = int(input())
answer = 0

if n < 100:
    answer = n
else:
    for i in range(100, n+1):
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            answer += 1
    answer += 99

print(answer)