import itertools

while True:
    input_num = list(map(int,input().split()))
    if input_num[0] == 0:
        break
    else:
        k = input_num[0]
        s = input_num[1:len(input_num)]
        number = itertools.combinations(s, 6)
        for i in itertools.combinations(s, 6):
            print(* list(i))
        print()