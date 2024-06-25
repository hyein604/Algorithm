# 딕셔너리 사용

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
candidate = (list(map(int, input().split())))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


for target in candidate:
    print(count.get(target, 0), end=" ")