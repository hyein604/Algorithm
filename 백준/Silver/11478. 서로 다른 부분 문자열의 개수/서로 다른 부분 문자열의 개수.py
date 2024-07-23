s = list(input())

hashTable = {}

for i in range(len(s)):
    for j in range(i, len(s)):
        subString = ''.join(s[i: j+1])

        if subString in hashTable.keys():
            hashTable[subString] += 1
        else:
            hashTable[subString] = 1

print(len(hashTable))