m, n = map(int, input().split())    # 조카 수, 과자 수
length = list(map(int, input().split()))    # 과자들 길이

s = 1
e = max(length)
answer = 0

while s <= e:
    mid = (s+e) // 2

    pass_sign = 0
    for cookie in length:
        if cookie - mid >= 0:
            pass_sign += cookie // mid

    if pass_sign >= m:
        answer = max(answer, mid)
        s = mid + 1
    elif pass_sign < m:
        e = mid - 1

print(answer)