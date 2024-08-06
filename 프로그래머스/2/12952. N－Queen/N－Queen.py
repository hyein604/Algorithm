def solution(n):
    global answer
    v1 = [0 for _ in range(n)]  # 열
    v2 = [0 for _ in range(n * 2)]  # 대각선 상방
    v3 = [0 for _ in range(n * 2)]  # 대각선 하방
    answer = 0

    def dfs(num):
        global answer
        if num == n:
            answer += 1
            return

        for i in range(n):
            if v1[i] == v2[num + i] == v3[num - i] == 0:
                v1[i] = v2[num + i] = v3[num - i] = 1
                dfs(num + 1)
                v1[i] = v2[num + i] = v3[num - i] = 0

    dfs(0)
    return answer