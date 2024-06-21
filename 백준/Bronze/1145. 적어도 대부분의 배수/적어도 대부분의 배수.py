numlist=[] #입력받은숫자

#입력받기
numlist=list(map(int,input().split()))


for i in range(1,1000000): #100
    cnt=0
    for j in range(4+1):
      if i%numlist[j]==0:
         cnt +=1
    if cnt>2:
      answer=i
      break

print(answer)