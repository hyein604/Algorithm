count = 0

N = int(input()) #6

for i in range(1,N+1):
        for j in range(1, N+1):
            if i-j >= 2: # 남규(i)는 영훈(j)이 보다 2개 이상 많이 받았으면 통과
                for k in range(1, N+1):
                    if N == i+k+j and k % 2 == 0: # 남은 사탕이 없고 택희가 짝수개 받았으면 통과
                        count += 1

print(count)
