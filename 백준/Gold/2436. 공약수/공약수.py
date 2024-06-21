g, l = map(int, input().split())

# 최대 공약수
def gcd(a,b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

# 최소 공배수
def lcm(a,b):
    return a*b//gcd(a,b)

div = l//g
a, b = 1, div
for i in range(1, div//2 + 1):
    if div % i == 0:
        c = i
        d = div//i
        if gcd(c,d) != 1:
            continue
        if a+b > c+d:
            a = c
            b = d

print(a*g, b*g)