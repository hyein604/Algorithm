N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
tmp = []

def recur(idx, arr_sum):
    global count
    if idx == N:
        if arr_sum == S:
            count += 1
        return

    # 정수 선택 했을때
    tmp.append(arr[idx])
    recur(idx+1, arr_sum + arr[idx])
    tmp.pop()
    # 정수 선택 안했을때
    recur(idx + 1, arr_sum)


recur(0,0)
if S == 0:
    count -= 1
print(count)