A,B = map(int,input().split())
A -= 1
tmpA=0
tmpA += A
for i in range(1,99):
    tmpA += (A//(2**i))*((2**i)-(2**(i-1)))
tmpB=0
tmpB += B
for i in range(1,99):
    tmpB += (B//(2**i))*((2**i)-(2**(i-1)))
    
print(tmpB - tmpA)