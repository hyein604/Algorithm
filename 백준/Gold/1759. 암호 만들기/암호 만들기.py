l, c = map(int, input().split())    # 암호길이, 후보 문자 개수
letters = sorted(list(map(str, input().split())))   # 후보 문자
arr = []


# 모음 세는 함수
def count_vowel(lst):
    return lst.count('a') + lst.count('e') + lst.count('i') + lst.count('o') + lst.count('u')


def recur(idx):
    if len(arr) == l:
        # 모음 한개이상, 자음 두개 이상이면
        if count_vowel(arr) >= 1 and l - count_vowel(arr) >= 2:
            # if arr not in answer:
            print("".join(arr))
            return

    for i in range(idx, c):
        arr.append(letters[i])
        recur(i + 1)
        arr.pop()

recur(0)