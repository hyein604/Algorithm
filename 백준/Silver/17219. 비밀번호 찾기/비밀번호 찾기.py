n, m = map(int, input().split())    # 사이트 주소 수, 비밀번호 찾으려는 사이트 주소
memo = {}
for _ in range(n):
    address, pw = map(str, input().split())
    memo[address] = pw

for _ in range(m):
    find_address = input()
    print(memo[find_address])