import sys
input = sys.stdin.readline

MAX_NUM = 1000001

nums = [0 for _ in range(MAX_NUM)]
end = int(MAX_NUM**0.5)
mul = 2

def isPrime(num):
    end = int(num ** 0.5)
    n = 2

    while n <= end:
        if num % n == 0: return False
        n += 1
    
    return True


while mul <= end:
    if not nums[mul]: 
        start = mul
        if isPrime(mul): start = mul*2

        for m in range(start, MAX_NUM, mul):
            nums[m] = 1
    mul += 1

pnums = []
for i in range(3, MAX_NUM): 
    if not nums[i]: pnums.append(i)

while True:
    t = int(input())
    if t == 0: break
    pidx = 0
    state = False

    while pnums[pidx] < t:
        if not nums[t - pnums[pidx]]:
            state = True
            break
        pidx += 1
    if pnums[pidx] < t - pnums[pidx]:
        a = pnums[pidx]
        b = t - pnums[pidx]
    else:
        a = t - pnums[pidx]
        b = pnums[pidx]

    if state: print(f"{t} = {a} + {b}")
    else: print("Goldbach's conjecture is wrong.")