tc = int(input())

answer = 0

for _ in range(tc):
    word = input()
    error = False

    for i in range(len(word)-2):
        if word[i] in word[i+2:]:
            if word[i] != word[i+1]:
                error = True
                break

    if not error:
        answer += 1

print(answer)