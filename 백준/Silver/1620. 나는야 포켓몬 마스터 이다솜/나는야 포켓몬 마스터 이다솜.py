n, m = map(int, input().split())    # 포켓몬 수, 맞춰야하는 문제
pocketmon = {}

# 포켓몬 도감 만들기
for i in range(1, n + 1):
    input_pocketmon = input()
    pocketmon[i] = input_pocketmon
    pocketmon[input_pocketmon] = i

# 문제 풀기
for _ in range(m):
    question = input()

    if question.isdigit():
        print(pocketmon[int(question)])
    else:
        print(pocketmon[question])