import sys
input = sys.stdin.readline

n, k = map(int, input().split())

words = []
alpha = [0 for _ in range(26)]

for _ in range(n):
    word = input()[:-1]

    for c in list(word):
        if alpha[ord(c) - ord('a')]: continue
        alpha[ord(c) - ord('a')] = 1

    words.append(word)

ans = 0

def combination(idx, cnt):
    global n, k, ans

    if cnt == k:
        matchedCnt = 0

        for i in range(n):
            state = True 

            for w in words[i]:
                idx = ord(w) - ord('a')
                if not selectedAlpah[idx]:
                    state = False
                    break

            if state: matchedCnt += 1

        ans = max(ans, matchedCnt)
        return
    
    for i in range(idx, 26):
        if not selectedAlpah[i]:
            selectedAlpah[i] = 1
            combination(i, cnt + 1)
            selectedAlpah[i] = 0

selectedAlpah = [0 for _ in range(26)]
if k >= 5:
    for c in ['a', 'c', 'i', 'n', 't']:
        selectedAlpah[ord(c) - ord('a')] = 1

    combination(0, 5)

elif k == 26:
    ans = n

print(ans)

# anta rc tica
# anta hello tica
# anta car tica

# abcdefg

# a c n t i (r)


# a c n t i () () ()
# 3
# anta b tica
# anta x tica
# anta d tica
# anta e tica
# anta f tica
# anta g tica
# anta h tica
# anta j tica
# anta k tica

# cnt = k개의 알파벳으로 만들 수 있는 단어 수
# -> max cnt 를 구하라
# [4: len(arr) - 4]

# 1. assign alphabet dict to each row 
# 2. 

# a b c d e f ...

