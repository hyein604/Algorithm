n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    answer = 0
    # 이분탐색
    s = 0
    e = n - 1

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == target:
            answer = 1
            break
        elif target < arr[mid]: # 다운
            e = mid - 1
        else:
            s = mid + 1

    print(answer)