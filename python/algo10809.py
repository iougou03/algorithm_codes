string = list(input())
alphaIdx = [-1 for _ in range(26)]

for char in string:
    idx = ord(char) - ord('a')
    if alphaIdx[idx] == -1:
        alphaIdx[idx] = string.index(char)

print(*alphaIdx)
