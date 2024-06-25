N=int(input())
num1 = 0
num2 = 1
answer = 0
def recur(count):
    global num1, num2, answer
    if count == N and N != 1:
        print(answer)
        return
    if N == 0:
        print(0)
        return
    if N == 1:
        print(1)
        return
    answer = num1 + num2
    num1 = num2
    num2 = answer
    recur(count+1)

recur(1)