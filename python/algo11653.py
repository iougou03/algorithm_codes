n = int(input())

mul = 2

while n > 1:
    while n % mul == 0:
        print(mul)
        n //= mul
    mul += 1
