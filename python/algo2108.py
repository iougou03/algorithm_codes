# import random
# import sys

# N = int(sys.stdin.readline())
# seq = [] ; sum = 0 ; mode_list = [0 for _ in range(8001)]
# max_val = -4000 ; min_val = 4000

# # -4000 <= v <= 4000 -> 8001
# for i in range(N):
#     seq.append(int(sys.stdin.readline()))
#     sum += seq[i]
#     mode_list[seq[i] + 4000] += 1
#     max_val = max(seq[i], max_val) ; min_val = min(seq[i], min_val)

# arithmetic_mean = sum // N + round((sum % N) / N + 1) - 1

# seq2 = sorted(set(seq)) ; seq2_len = len(seq2)
# seq2 = iter(seq2)
# for i in range(seq2_len // 2): next(seq2)
# median = next(seq2)

# twice = False ; mode_idx = 0

# for i in range(len(mode_list)):
#     if mode_list[mode_idx] < mode_list[i]:
#         mode_idx = i ; twice = False
#     elif mode_list[mode_idx] == mode_list[i] and not twice:
#         mode_idx = i ; twice = True

# period = abs(max_val - min_val)
# print(arithmetic_mean)
# print(median)
# print(mode_idx - 4000)
# print(period)

# ------------------------------
# def sample_maker(n):
#     sample_list = []
#     for i in range(n):
#         neg = False if int(random.random() * 10) % 2 == 0 else True 
#         val = int(random.random() * 1000) % 10
#         if neg: val *= -1
#         sample_list.append(val)
#     return sample_list
# n = 20
# print(n)
# [print(sm) for sm in sample_maker(n)]

# version 1.
import sys

N = int(sys.stdin.readline())
seq = [] ; sum = 0 ; mode_list = [0 for _ in range(8001)]
max_val = -4000 ; min_val = 4000

# -4000 <= v <= 4000 -> 8001
for i in range(N):
    seq.append(int(sys.stdin.readline()))
    sum += seq[i]
    mode_list[seq[i] + 4000] += 1
    max_val = max(seq[i], max_val) ; min_val = min(seq[i], min_val)

arithmetic_mean = round(sum / N)

seq.sort()
median = seq[N // 2]

twice = False ; mode_idx = 0

for i in range(1, len(mode_list)):
    if not mode_list[i]: continue
    if mode_list[mode_idx] < mode_list[i]:
        mode_idx = i
        twice = False
    elif mode_list[mode_idx] == mode_list[i] and not twice:
        mode_idx = i
        twice = True

period = max_val - min_val

print(arithmetic_mean)
print(median)
print(mode_idx - 4000)
print(period)