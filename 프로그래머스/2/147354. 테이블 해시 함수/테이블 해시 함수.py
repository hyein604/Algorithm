def solution(data, col, row_begin, row_end):
    answer = 0
    s_i = []
    data = sorted(data, key=lambda x : [x[col - 1], -x[0]])

    for i in range(row_begin-1, row_end):
        s_i_num = 0
        for num in data[i]:
            s_i_num += num % (i+1)
        s_i.append(s_i_num)

    for num in s_i:
        answer ^= num

    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))