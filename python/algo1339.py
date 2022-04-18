n = int(input())
problems = []
for _ in range(n): 
    problems.append(input().rstrip())

# version2
alphabet = {}

for pro in problems:
    for i in range(len(pro)):
        if pro[i] not in alphabet:
            alphabet[pro[i]] = 10**(len(pro) - 1 - i)
        else:
            alphabet[pro[i]] += 10**(len(pro) - 1 - i)

sortKeys = sorted(alphabet, key = alphabet.get, reverse=True)
num = 9
for key in sortKeys:
    alphabet[key] = str(num)
    num -= 1

ans = 0
for pro in problems:
    strNum = ''
    for c in list(pro):
        strNum += alphabet[c]
    ans += int(strNum)

print(ans)

# verison 1. error code
# alphabet = {
#     "A":0,
#     "B":0,
#     "C":0,
#     "D":0,
#     "E":0,
#     "F":0,
#     "G":0,
#     "H":0,
#     "I":0,
#     "J":0,
# }

# for pro in problems:
#     for i in range(len(pro)):
#         alphabet[pro[i]] = max(alphabet[pro[i]], len(pro) - i)

# sortKeys = sorted(alphabet, key = alphabet.get, reverse=True)
# num = 9
# for key in sortKeys:
#     alphabet[key] = str(num)
#     num -= 1

# ans = 0
# for pro in problems:
#     numStr = ''
#     for c in list(pro):
#         numStr += alphabet[c]
#     print(numStr)
#     ans += int(numStr)

# print(ans)

# -> 반례 : 낮은 자리수에 있는 알파벳이 훨씬 많이 나온다면?