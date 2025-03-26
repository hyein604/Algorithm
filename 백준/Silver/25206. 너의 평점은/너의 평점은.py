score_table ={'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

total_score = 0.0
total_credit = 0.0

for _ in range(20):
    subject_name, credit, score = map(str, input().split())
    if score == 'P':
        continue
    else:
        total_credit += float(credit)
        total_score += float(credit) * score_table[score]

answer = total_score / total_credit
print(answer)