def recur(idx, sin, ssun, choose_num):

    if idx == n:
        if choose_num != 0:
            global answer
            answer = min(answer, abs(sin - ssun))
        return
    #재료사용x
    recur(idx+1,sin,ssun, choose_num)
    #재료사용o 
    recur(idx+1,sin*ingredient[idx][0],ssun+ingredient[idx][1], choose_num+1)

n = int(input())

ingredient=[[] for _ in range(n)]
for i in range(n):
    a,b = map(int, input().split())
    ingredient[i] = [a,b]


answer = 9999999999999999

recur(0, 1, 0, 0)
print(answer)