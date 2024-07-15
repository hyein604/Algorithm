n, m = map(int, input().split())    # 바구니 수, 역순 횟수
basket = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp

print(*basket)