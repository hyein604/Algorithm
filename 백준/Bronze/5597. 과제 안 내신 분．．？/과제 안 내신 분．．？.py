answer = [i for i in range(1, 30 + 1)]
for _ in range(28):
    attend = int(input())
    answer.remove(attend)

sorted(answer)

for answer_num in answer:
    print(answer_num)