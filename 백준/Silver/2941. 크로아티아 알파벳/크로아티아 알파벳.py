word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0

for croatia_alphabet in croatia:
    while croatia_alphabet in word:
        if croatia_alphabet in word:
            answer += word.count(croatia_alphabet)
            word = word.replace(croatia_alphabet,'*')

word = word.replace("*",'')
answer += len(word)
print(answer)