N = int(input())
F = int(input())
number = list(map(int, str(N)))

#1의자리수 빼기
for i in range (1,10):
    if number[-1] == 0:
        break
    if number[-1] == i:
        N = N - i
        break

#10의 자리수 빼기
for i in range (1,10):
    if number[-2] == 0:
        break
    if number[-2] == i:
        N = N - i*10
        break

for i in range(99+1):
    N += i
    if N % F == 0:
        break
    N -= i

answer=list(map(int,str(N)))

print(answer[-2],answer[-1],sep='')