tc = int(input())

for _ in range(tc):
    n = int(input())  # 가진 의상 수
    closet = {}

    for _ in range(n):
        name, category = map(str, input().split())

        if category not in closet:
            closet[category] = [name]

        else:
            closet[category].append(name)

    answer = 1
    for names in closet.values():
        answer *= len(names) + 1
    answer -= 1

    print(answer)