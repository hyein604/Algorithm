def solution(n, results):
    answer = 0
    win_lose = [[0] * n for _ in range(n)]

    for a, b in results:
        # board의 인덱스는 선수번호 - 1
        # 1은 승리
        # -1은 패배
        win_lose[a - 1][b - 1] = 1
        win_lose[b - 1][a - 1] = -1

    # 모든 사람과 서로 겨뤄보면서 승패 기록
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or win_lose[i][j] in [1, -1]:    # 나 자신이거나 승리 또는 패배 기록 있으면 패스
                    continue
                if win_lose[i][k] == win_lose[k][j] == 1:
                    win_lose[i][j] = 1
                    win_lose[j][i] = win_lose[k][i] = win_lose[j][k] = -1

    for player in win_lose:
        if player.count(0) == 1:   # 모든사람과 겨뤄봐서 나빼고 승패결과가 있다면
            answer += 1
    return answer