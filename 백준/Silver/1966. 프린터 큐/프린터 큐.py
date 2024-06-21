from collections import deque
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())    # 문서개수, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지
    important = deque(map(int, input().split()))
    mark = deque(0 for _ in range(n))
    mark[m] = 1
    answer_import = []
    answer_mark = []

    while important:
        left_pop_important = important.popleft()
        left_pop_mark = mark.popleft()

        if not important:
            answer_import.append(left_pop_important)
            answer_mark.append(left_pop_mark)
        else:
            if left_pop_important >= max(important):
                answer_import.append(left_pop_important)
                answer_mark.append(left_pop_mark)
            else:
                for important_num in important:
                    if left_pop_important <= important_num:
                        important.append(left_pop_important)
                        mark.append(left_pop_mark)
                        break

    print(answer_mark.index(1) + 1)