max_ans = -1000000000
min_ans = 1000000000

def add(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b): 
    if a < 0:
        return (abs(a) // b) * -1
    return a // b

def solution(val, level):
    global max_ans, min_ans

    if level == N - 1:
        max_ans = max_ans if max_ans > val else val
        min_ans = min_ans if min_ans < val else val
        return

    for i in range(4):
        if oper_list[i]:
            oper_list[i] -= 1
            solution(oper_dict[str(i)](val, seq[level + 1]), level + 1)
            oper_list[i] += 1 # <- ★★★ key code

N = int(input())

seq = list(map(int, input().split()))

# + - × ÷
oper_dict = {
    "0":add,
    "1":sub,
    "2":mul,
    "3":div,
}
oper_list = list(map(int, input().split()))

solution(seq[0], 0)

print(max_ans)
print(min_ans)