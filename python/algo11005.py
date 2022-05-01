num, radix = map(int, input().split())

def translate(n):
    if n >= 10:
        return chr(ord("A") + (n - 10))
    else:
        return n

def radixTrasnlator(decimalNum, radix):
    digits = []
    while decimalNum > 0:
        digits.append(translate(decimalNum % radix))
        decimalNum //= radix

    return digits

ans = radixTrasnlator(num, radix)
while ans:
    print(ans.pop(), end="")
        
    
