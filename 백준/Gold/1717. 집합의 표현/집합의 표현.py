import sys
input = sys.stdin.readline

# 예시 : par[1]=2 -> 1의 조상은 2이다.
par = [i for i in range(1000001)]
#집합의 깊이를 나타내는 배열인가? (수업시간 : 1칸이다!)
rank = [1 for _ in range(1000001)]

#원소의 조상 확인하는 함수 -> 원소가 어느 집합에 포함되어있는지 확인가능
def _find(a):
    if par[a] == a:
        return a
    else:
        par[a] = _find(par[a])
        return par[a]
    
def _union(a,b):
    a = _find(a)
    b = _find(b)

    #이미 같은 트리에 속하면 합치지 않는다
    if a == b:
        return
    
    #더 짧은 트리가 긴 트리에 합쳐지도록 하기
    if rank[a] == rank[b]:
        par[a] = b
        rank[b] += 1
    elif rank[a] < rank[b]:
        par[a] = b
    elif rank[b] < rank[a]:
        par[b] = a

# n : n+1개 집합 {0}, {1}, {2}, ... , {n}
# m : 입력으로 주어지는 연산의 개수
n,m=map(int,input().split())

# for i in range(m):
#     tmp = list(map(int,input().split()))
#     inputList.append(tmp)

for _ in range(m):
    # 0 a b : a가 포함되어있는 집합과 b가 포함되어 있는 집합 합침
    # 1 a b : a와 b가 같은 집합에 포함되어있는지 확인
    k, a, b = map(int, input().split())

    if k == 0:
        _union(a,b)
    elif k == 1:
        if _find(a) == _find(b):
            print("YES")
        else:
            print("NO")