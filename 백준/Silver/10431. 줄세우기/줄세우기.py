N = int(input())

for i in range(1, N+1):
    count = 0
    sorted_height = []
    height = list(map(int, input().split()))
    sorted_height.append(height[1])

    for j in range(2, 20+1):
        for k in range(len(sorted_height)):
            if height[j] < sorted_height[k]:
                count += len(sorted_height) - k
                sorted_height.insert(k, height[j])
                break
            else:
                if k == len(sorted_height)-1:
                    sorted_height.append(height[j])

    print(i, count)