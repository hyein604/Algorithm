k, m = map(int, input().split())    # 이미 있는 랜선 수, 필요한 랜선
length = []
for _ in range(k):
    length.append(int(input()))
answer = 0
s = 1
e = max(length)

while s <= e:
    mid = (s + e) // 2

    line_count = 0      # mid 길이로 잘랐을때 나오는 랜선 수
    for line in length:
        line_count += line // mid

    if line_count == m:
        answer = max(answer, mid)
        s = mid + 1
    elif line_count > m:
        answer = max(answer, mid)
        s = mid + 1
    elif line_count < m:
        e = mid - 1

print(answer)