def solution(n, times):
    answer = 0
    # s(start), e(end) 투포인터!
    s = 1
    e = max(times) * n

    while s <= e:   # 교차될때 스탑
        mid = (s+e) // 2
        check_person = 0
        for time in times:
            check_person += mid // time  # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            if check_person >= n:
                break

        #업?
        if check_person >= n:
            e = mid - 1
            answer = mid
        # 다운?
        else:
            s = mid + 1

    return answer