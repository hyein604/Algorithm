N = int(input())
S = list(map(int,input().split()))
numbers = []
tmp = 0
answer = 0

def recur(idx, sum):
    if idx == len(S):
        numbers.append(sum)
        return
    # 숫자 선택 했으면
    recur(idx+1, sum + S[idx])

    # 숫자 선택 안했으면
    recur(idx+1, sum)


recur(0,0)
numbers.sort()
# print(numbers)
for i in range(len(numbers)):
    if numbers[i] <= tmp:
        tmp = numbers[i]+1
    else:
        answer = tmp
        break

if answer == 0:
    print(numbers[-1]+1)
else:
    print(answer)