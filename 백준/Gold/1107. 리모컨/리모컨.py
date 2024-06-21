target = int(input())
m = int(input())
if m != 0:
    broken = list(map(int, input().split()))
else:
    broken = []

count = abs(100 - target)

for num in range(1000000 + 1):
    for n in str(num):
        if int(n) in broken:
            break
    else:
        count = min(count, len(str(num)) + abs(num - target))

print(count)
