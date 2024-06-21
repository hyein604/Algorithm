n = int(input())

if n > 1022:
    print(-1)
else:
    num = []
    ans = []

    def decrease(i):
        global num
        if len(num) == 1:
            return True
        if num[-2] > i:
            return True


    def dfs(idx):
        global num

        for i in range(9 + 1):
            num.append(i)
            if decrease(i):
                dfs(idx + 1)
                ans.append(int(''.join(str(x) for x in num)))
            num.pop()

    dfs(0)
    ans.sort()

    print(ans[n])