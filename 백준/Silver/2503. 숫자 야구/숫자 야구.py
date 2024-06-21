question_list=[] #입력받은 수의 리스트
s_list=[]
b_list=[]
count=0 #경우의수


def strike(i, question):
    strike = 0

    i_num_1 = i // 100
    i_num_2 = i % 100 // 10
    i_num_3 = i % 10

    q_num_1 = question // 100
    q_num_2 = question % 100 // 10
    q_num_3 = question % 10

    if i_num_1 == q_num_1:
        strike += 1
    if i_num_2 == q_num_2:
        strike += 1
    if i_num_3 == q_num_3:
        strike += 1

    return strike


# 볼 수 구하기
def ball(i, question):
    ball = 0

    i_num_1 = i // 100
    i_num_2 = i % 100 // 10
    i_num_3 = i % 10

    q_num_1 = question // 100
    q_num_2 = question % 100 // 10
    q_num_3 = question % 10

    if i_num_1 == q_num_2 or i_num_1 == q_num_3:
        ball += 1
    if i_num_2 == q_num_1 or i_num_2 == q_num_3:
        ball += 1
    if i_num_3 == q_num_2 or i_num_3 == q_num_1:
        ball += 1

    return ball


#입력받기
N=int(input())

for _ in range(N):
    question,s,b = map(int,input().split())
    question_list.append(question)
    s_list.append(s)
    b_list.append(b)

#111~999를 입력받은 수와 스트라이크,볼 비교
for i in range(111,999):
    tmp = 0 

    #자리수 같으면 패쓰
    if i//100 == i%100//10 or i//100 == i%10 or i%100//10 == i%10:
        continue
    if i%100//10 == 0 or i%10 ==0:
        continue

    for j in range(N):
        if strike(i,question_list[j])==s_list[j] and ball(i,question_list[j])==b_list[j]:
            tmp += 1
    if tmp == N:
        count += 1

    
#출력
print(count)