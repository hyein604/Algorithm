mushroom = []
score = 0

for i in range(10):
    mushroom.append(int(input()))

for i in range(10):
    score += mushroom[i]
    if i != len(mushroom)-1:
        if abs(100 - score) > abs(100 - score - mushroom[i+1]):
            continue
        elif abs(100 - score) == abs(100 - score - mushroom[i+1]):
            score += mushroom[i+1]
            break
        elif abs(100 - score) < abs(100 - score - mushroom[i+1]):
            break
    else:
        continue
print(score)