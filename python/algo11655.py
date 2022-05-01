string = input()

def encrypt(string):
    s = ""
    for char in string:
        if ord("a") <= ord(char) <= ord("z"):
            s += chr(ord("a") + (ord(char) - ord("a") + 13) % 26)
        elif ord("A") <= ord(char) <= ord("Z"):
            s += chr(ord("A") + (ord(char) - ord("A") + 13) % 26)
        else:
            s += char

    return s        
    

print(encrypt(string))