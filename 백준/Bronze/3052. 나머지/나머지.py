arr = []
count = 0
for i in range(10):
    a = int(input())
    arr.append(a%42)
for i in range(1000):
    if i in arr:
        count += 1
print(count)