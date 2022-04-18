import sys

N = int(sys.stdin.readline())
seqxy = []

for _ in range(N):
    seqxy.append(list(map(int, sys.stdin.readline().split())))

seqxy.sort(key = lambda x: x[0])
seqxy.sort(key = lambda x: x[1])

# val = seqxy[0][1] ; end = 0 ; start = 0
# for i in range(1, N):
#     if val != seqxy[i][1]:
#         val = seqxy[i][1]
#         if end:
#             seqxy = seqxy[:start] + sorted(seqxy[start: end + 1], key = lambda x: x[0]) + seqxy[end + 1:]
#             end = 0 
#         start = i
#     else: # val == seqxy
#         end = i

[print(x,y) for x,y in seqxy]