alphaCnt = [0 for _ in range(26)]

string = input()

for char in string:
    alphaCnt[ord(char) - ord('a')] += 1

print(*alphaCnt)