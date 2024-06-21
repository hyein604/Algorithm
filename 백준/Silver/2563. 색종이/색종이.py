answer=0
#종이넓이 가로,세로 배열만들고 다 0 채우기
paper=[[0 for _ in range(100)] for _ in range(100)] 


#색종이 위치받으면 색종이 넓이를 종이 넓이 배열에 +1
N=int(input()) #색종이개수 입력받기
for _ in range(N): 
    w, l = map(int, input().split())
    for i in range(0,10):
        for j in range(0,10):
            paper[w+j][l+i] += 1


#종이넓이 배열 다 돌면서 1이상인부분 발견되면 answer+1. answer출력
for i in range(100):
    for j in range(100):
        if  paper[i][j]>=1:
            answer += 1
        
print(answer)