n = int(input())

num1 = 0
num2 = 1
answer = 0

def recur(cnt):
    global num1, num2, answer

    if cnt == n and n != 1:
        print(answer)
        return

    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return

    answer = num1 + num2
    num1 = num2
    num2 = answer
    recur(cnt + 1)

recur(1)