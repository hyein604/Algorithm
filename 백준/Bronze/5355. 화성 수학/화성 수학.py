N = int(input())

for i in range(N):
    arr = list(map(str, input().split()))
    answer = float(arr[0])
    for j in range(1,len(arr)):
        if arr[j] == '@':
            answer = answer * 3
        elif arr[j] == '%':
            answer = answer + 5
        elif arr[j] == '#':
            answer = answer - 7
    print(format(answer, '.2f'))