N = int(input())
numbers = []
check = True
# N이 1인 경우 아무것도 출력하지 않는다.
if N == 1:
    print()

#소수인지 확인하는 함수. 소수면 True, 소수아니면 False
def checkDecimal(number):
    global check
    for i in range(2,number):
        if number % i == 0:
            check = False
            break
    return check

def recur(num):
    if num == 0 or num == 1:
        sorted(numbers)
        return numbers

    for i in range(2,num+1):
        if num % i ==0 and checkDecimal(i) == True:
            numbers.append(i)
            recur(num // i)
            return

recur(N)

for i in numbers:
    print(i)