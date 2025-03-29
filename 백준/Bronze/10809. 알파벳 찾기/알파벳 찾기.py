word = input()
alphabet = [-1 for _ in range(26)]

for letter in word:
    alphabet[ord(letter)-97] = word.index(letter)

print(*alphabet)