import timeit
N = 10000000

start = timeit.default_timer()
fact = [1 for _ in range(N)]

for i in range(N):
    fact[i] *= fact[i - 1] * i

stop = timeit.default_timer()

print(stop - start)