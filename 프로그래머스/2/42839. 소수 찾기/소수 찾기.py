import itertools

def sosu(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = []
    for i in range(len(n)):
        number = set(map(int, map("".join, itertools.permutations(list(n), i + 1))))

        for num in number:
            if sosu(num):
                answer.append(num)

    return len(set(answer))