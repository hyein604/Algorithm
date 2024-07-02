N, M = map(int,input().split())
numbers=sorted(list(map(int,input().split())))
answer = []
def recur(idx):
    if len(answer) == M:
        print(* answer)
        return

    for i in numbers:
        if i not in answer and i > idx:
            answer.append(i)
            idx = i
            recur(idx)
            answer.pop()
recur(0)