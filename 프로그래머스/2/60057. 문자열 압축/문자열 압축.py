def solution(s):
    result = []

    for i in range(1, len(s) + 1):
        compression_text = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s) + i, i):
            if tmp == s[j : i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    compression_text += str(cnt) + tmp
                else:
                    compression_text += tmp
                tmp = s[j : j + i]
                cnt = 1

        result.append(len(compression_text))

    return min(result)