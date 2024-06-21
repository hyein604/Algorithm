N=int(input())
list=[]

for i in range(N):
    S=int(input())
    list.append(S)

for i in list:
    for j in range(2, 10**6 + 1):
        if i % j != 0:
            if j != 10**6:
                continue
            else:
                print("YES")
                break
        else:
            print("NO")
            break