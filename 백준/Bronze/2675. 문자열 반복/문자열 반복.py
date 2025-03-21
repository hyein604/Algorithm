tc = int(input())

for _ in range(tc):
    R, S = map(str, input().split())
    answer = ''
    for letter in S:
        for i in range(int(R)):
            answer += letter
    print(answer)