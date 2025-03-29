n, m = map(int, input().split())    # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
hash_map = {}
answer_lst = []
# 듣도 못한 사람 이름 명단
for _ in range(n + m):
    name = input()
    if name in hash_map.keys():
        hash_map[name] += 1
    else:
        hash_map[name] = 1

for name in hash_map.keys():
    if hash_map[name] == 2:
        answer_lst.append(name)

answer_lst.sort()

print(len(answer_lst))
for answer in answer_lst:
    print(answer)