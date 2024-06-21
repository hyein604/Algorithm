from itertools import *
answer = []
nine_dwarfs = [int(input()) for _ in range(9)]

# 아홉 명의 난쟁이 중에서 일곱 명을 선택하여 합이 100이 되는지 확인
for seven_dwarfs in combinations(nine_dwarfs, 7):
    if sum(seven_dwarfs) == 100:
        # 합이 100이면 정답을 오름차순으로 출력
        for answer in sorted(seven_dwarfs):
            print(answer)
        break