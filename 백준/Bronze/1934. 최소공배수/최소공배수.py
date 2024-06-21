N = int(input())
# 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 구하기
for i in range(N):
    A, B = map(int,input().split())
    print(int(A * B / gcd(A,B)))