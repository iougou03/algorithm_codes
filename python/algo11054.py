N = int(input())
inc_max = [0 for _ in range(N + 1)]
dec_max = [0 for _ in range(N + 1)]
ans = 0
# time complexity O(N^2)
def inc(idx):
    max_idx = 0
    for i in range(idx):
        val = seq[idx]
        if val > seq[i]:
            max_idx = max_idx if inc_max[max_idx] > inc_max[i + 1] else i + 1
    inc_max[idx + 1] = inc_max[max_idx] + 1

def dec(idx):
    max_idx = 0
    for i in range(idx):
        val = seq_reverse[idx]
        if val > seq_reverse[i]:
            max_idx = max_idx if dec_max[max_idx] > dec_max[i + 1] else i + 1
    dec_max[idx + 1] = dec_max[max_idx] + 1

seq = list(map(int, input().split()))
seq_reverse = seq.copy()
seq_reverse.reverse()

for i in range(N):
    inc(i)
    dec(i)

dec_max.reverse()
for i in range(1,N + 1):
    ans = max(inc_max[i] + dec_max[i -1] - 1, ans)
print(ans)