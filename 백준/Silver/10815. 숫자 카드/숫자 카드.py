n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for number in arr2:
    # s, e 투포인터
    s = 0
    e = n - 1
    flag = False

    while s <= e:
        mid = (s + e) // 2
        # 정답인가요?
        if arr1[mid] == number:
            flag = True
            break

        # 업?
        elif arr1[mid] > number:
            e = mid - 1

        # 다운?
        elif arr1[mid] < number:
            s = mid + 1

    if flag:
        print(1, end = ' ')
    else:
        print(0, end = ' ')