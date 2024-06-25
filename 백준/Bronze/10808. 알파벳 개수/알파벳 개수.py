word = list(input())
answer = []
for i in range(97,122+1):
    answer.append(word.count(chr(i)))
print(*answer)