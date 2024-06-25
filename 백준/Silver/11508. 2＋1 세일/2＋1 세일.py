N = int(input())
price_list = [int(input()) for _ in range(N)]
price_list.sort(reverse=True)
tmp = 0

for i in range(1,len(price_list)//3+1):
    tmp += price_list[3*i-1]

print(sum(price_list) - tmp)