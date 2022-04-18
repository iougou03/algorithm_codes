n, k = map(int, input().split())

def fact(n):
    if n <= 1: return 1
    return n * fact(n- 1) 

print(fact(n) // (fact(k) * fact(n - k)))