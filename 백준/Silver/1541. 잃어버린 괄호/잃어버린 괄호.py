formular = list(input().split('-'))
sub_operand = []

for summ in formular:
    sum_operand = sum(map(int, summ.split('+')))
    sub_operand.append(sum_operand)

answer = sub_operand[0]

for i in range(1, len(sub_operand)):
    answer -= sub_operand[i]

print(answer)