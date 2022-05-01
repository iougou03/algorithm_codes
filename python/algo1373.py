# bin_num = list(input())

# octa = []
# temp = []

# def get_oct(bin3):
#     val = 0
#     for i in range(len(bin3)):
#         if bin3[i] == "1":
#             val += 2**i
#     return val

# while bin_num:
#     if len(temp) < 3:        
#         temp.append(bin_num.pop())
#     else:
#         octa.append(str(get_oct(temp)))
#         temp = []

# if temp: octa.append(str(get_oct(temp)))
# octa.reverse()
# print("".join(octa))
        
binary = input()

num = int("0b"+binary, 2)
print(oct(num)[2:])