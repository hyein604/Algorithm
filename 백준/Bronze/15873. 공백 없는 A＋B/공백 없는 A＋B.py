n = list(input())

answer = 0

for idx in range(len(n) - 1):
    if n[idx] == '0':
        continue

    if n[idx + 1] != '0':
        operand = int(''.join(n[idx]))
    else:
        operand = int(''.join(n[idx:idx + 2]))

    answer += operand

print(answer + int(''.join(n[-1])))