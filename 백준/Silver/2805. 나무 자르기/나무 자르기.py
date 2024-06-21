n, m = map(int, input().split())
forest = list(map(int, input().split()))
s = 1
e = max(forest)

while s <= e:   # 교차되기 전까지
    mid = (s+e) // 2

    # 얼마나 나무를 모았는가?
    wood = 0
    for tree in forest:
        if tree >= mid:
            wood += tree - mid

    # 업?
    if wood >= m:
        s = mid + 1
    # 다운?
    else:
        e = mid - 1

print(e)