s = list(input())
cnt = [0 , 0]
idx = 1 ; c = s[0]

while idx < len(s):
    if c != s[idx]:
        cnt[int(c)] += 1
        c = s[idx]
    idx += 1

cnt[int(c)] += 1
print(min(cnt))