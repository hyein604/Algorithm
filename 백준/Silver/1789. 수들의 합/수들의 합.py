S = int(input())
sum = 0
count = 0
for i in range(1, 4294967295):
    sum += i
    count += 1
    if sum > S:
        print(count-1)
        break