nA, nB = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
answer = []


for target in A:
    s = 0
    e = len(B) - 1
    include = False

    while s <= e:
        mid = (s + e) // 2

        if target == B[mid]:
            include = True
            break
        elif target > B[mid]:
            s = mid + 1
        else:
            e = mid - 1

    if not include:
        answer.append(target)

if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(*answer)