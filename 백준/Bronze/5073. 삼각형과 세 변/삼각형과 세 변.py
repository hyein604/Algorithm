a, b, c = 1, 1, 1

while a != 0 and b != 0 and c != 0:
    a, b, c = map(int, input().split())
    lines = [a, b, c]
    longest = max(lines)
    lines.remove(max(lines))
    if longest < lines[0] + lines[1]:
        if longest == lines[0] and longest == lines[1] and lines[0] == lines[1]:
            print("Equilateral")
        elif longest != lines[0] and longest != lines[1] and lines[0] != lines[1]:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        if longest == 0 and lines[0] == 0 and lines[1] == 0:
            break
        else:
            print("Invalid")