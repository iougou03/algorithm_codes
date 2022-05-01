import sys
input = sys.stdin.readline

MAX_NUM = 1000001
pnums = [1 for _ in range(MAX_NUM)]
end = int(MAX_NUM**0.5)
mul = 2

def check_prime(num):
    idx = 2 ; end = int(num**0.5)
    while idx <= end:
        if num % idx == 0: return False
        idx += 1
    
    return True

while mul <= end:
    start = mul
    if check_prime(mul):
        start += mul
    
    for m in range(start, MAX_NUM, mul):
        if not pnums[m]: continue
        pnums[m] = 0
    mul += 1

t = int(input())

def cnt_gold_bach(num):
    cnt = 0
    for i in range(2, num // 2 + 1):
        if pnums[i] and pnums[num - i]:
            cnt += 1
    
    return cnt


for _ in range(t):
    n = int(input())
    print(cnt_gold_bach(n))