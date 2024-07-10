while True:
    sentence = input()
    if sentence == '#':
        break

    answer = 0
    for letter in sentence:
        if letter in ['a','e','i','o','u','A','E','I','O','U']:
            answer += 1

    print(answer)